tablas = {
    "MON_WEAK":
    """CREATE TABLE IF NOT EXISTS MON_WEAK (
        COD_MON     TEXT PRIMARY KEY,
        DATOS       JSON
        );""",
    "MON_LANG":
    """CREATE TABLE IF NOT EXISTS MON_LANG (
        COD_MON     TEXT PRIMARY KEY,
        LANG        INTEGER,
        DATOS       JSON
        );"""
}
