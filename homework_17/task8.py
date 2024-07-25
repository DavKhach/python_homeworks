def update_settings(**kwargs):
    apply_settings(**kwargs)

def apply_settings(**settings):
    for key, value in settings.items():
        print(f"Setting {key} to {value}")

user_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "privacy": "high"
}

update_settings(**user_settings)
