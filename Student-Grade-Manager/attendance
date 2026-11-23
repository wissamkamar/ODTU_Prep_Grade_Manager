"""Devamsızlık mantığı (arayüzden bağımsız).
 
Kaynak: METU SFL DBE 2026-2027 Rules and Regulations, "Attendance" bölümü.
Limitler her dönem için ayrıdır ve dönem sonunda sıfırlanır. Limit aşılırsa
öğrenci EPE'ye giremez ve sınıfta kalır. Tam limit (örn. 40/40) aşım sayılmaz.
"""
from dataclasses import dataclass
 
TERMS = ("Fall", "Spring")
LEVELS = (1, 2, 3, 4, 5)
 
# Dönem -> kur seviyesi -> izin verilen devamsızlık saati
LIMITS = {
    "Fall":   {1: 50, 2: 40, 3: 40, 4: 40, 5: 30},
    "Spring": {1: 60, 2: 50, 3: 40, 4: 40, 5: 20},
}
_TERM_NO = {"Fall": 1, "Spring": 2}
 
 
def group_name(level: int, term: str) -> str:
    """Örn. (3, 'Fall') -> 'DBE301', (3, 'Spring') -> 'DBE302'."""
    return f"DBE{level}0{_TERM_NO[term]}"
 
 
def limit(level: int, term: str) -> int:
    return LIMITS[term][level]
 
 
@dataclass(frozen=True)
class Status:
    used: int
    total: int
 
    @property
    def remaining(self) -> int:
        return max(0, self.total - self.used)
 
    @property
    def over_by(self) -> int:
        return max(0, self.used - self.total)
 
    @property
    def exceeded(self) -> bool:
        return self.used > self.total
 
    @property
    def remaining_percent(self) -> int:
        """Kalan hakkın yüzdesi (arayüzdeki %76 = 38/50)."""
        return round(self.remaining / self.total * 100)
 
 
def status(level: int, term: str, used: int) -> Status:
    return Status(used=used, total=limit(level, term))
 
 
def failed_terms(records: dict) -> list:
    """records: {'Fall': (level, used), 'Spring': (level, used)}.
    Herhangi bir dönemde limit aşıldıysa o dönemlerin listesini döndürür;
    liste boş değilse öğrenci sınıfta kalır (EPE'ye giremez)."""
    return [t for t, (lvl, used) in records.items() if status(lvl, t, used).exceeded]
