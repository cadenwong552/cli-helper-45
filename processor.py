from typing import Dict, List, Any

class MatchStatsProcessor:
    """Processes gaming match telemetry using bit-packed bitwise flags."""
    
    ACHIEVEMENT_FLAGS = {
        "mvp": 1 << 0,
        "flawless": 1 << 1,
        "clutch": 1 << 2,
        "first_blood": 1 << 3,
    }

    @staticmethod
    def pack_match_data(kills: int, deaths: int, score: int, achievements: List[str]) -> str:
        flags = sum(MatchStatsProcessor.ACHIEVEMENT_FLAGS.get(a.lower(), 0) for a in achievements)
        packed = ((score & 0xFFFFFF) << 40) | ((kills & 0xFFFF) << 24) | ((deaths & 0xFFFF) << 8) | (flags & 0xFF)
        return f"GME-{packed:016X}"

    @staticmethod
    def unpack_match_data(token: str) -> Dict[str, Any]:
        if not token.startswith("GME-") or len(token) != 20:
            raise ValueError("Invalid telemetry token format")
        
        raw_val = int(token[4:], 16)
        score = (raw_val >> 40) & 0xFFFFFF
        kills = (raw_val >> 24) & 0xFFFF
        deaths = (raw_val >> 8) & 0xFFFF
        flags = raw_val & 0xFF

        unlocked = [
            name for name, bit in MatchStatsProcessor.ACHIEVEMENT_FLAGS.items()
            if flags & bit
        ]
        
        kd_ratio = round(kills / max(1, deaths), 2)
        
        return {
            "score": score,
            "kills": kills,
            "deaths": deaths,
            "kd_ratio": kd_ratio,
            "achievements": unlocked,
        }

    @classmethod
    def aggregate_session_summary(cls, tokens: List[str]) -> Dict[str, Any]:
        unpacked_matches = [cls.unpack_match_data(t) for t in tokens]
        total_kills = sum(m["kills"] for m in unpacked_matches)
        total_deaths = sum(m["deaths"] for m in unpacked_matches)
        total_score = sum(m["score"] for m in unpacked_matches)
        
        all_achievements = sorted(list({ach for m in unpacked_matches for ach in m["achievements"]}))
        
        return {
            "matches_played": len(tokens),
            "total_score": total_score,
            "overall_kd": round(total_kills / max(1, total_deaths), 2),
            "unique_achievements": all_achievements,
        }
