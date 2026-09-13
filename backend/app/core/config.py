class Settings:
    #1600kVA pano için eşik değerler(temsili)
    NORMAL_TEMP_MIN = 25.0
    NORMAL_TEMP_MAX = 55.0
    CRITICAL_TEMP = 85.0

    NORMAL_CURRENT_MIN = 800.0
    NORMAL_CURRENT_MAX = 1500.0
    CRITICAL_CURRENT = 2200.0

    NORMAL_HUMIDITY_MIN = 30.0
    NORMAL_HUMIDITY_MAX = 60.0

    PD_THRESHOLD = 30.0 # Kısmi deşarj (Partial Discharge) sınırı

settings = Settings()