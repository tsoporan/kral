from django.db.models import get_app, get_models

def load_models(appname="kral", plugins=[]):
    """Load the plugins models if provided, else load them all."""
    app = get_app(appname)
    models = get_models(app)
    if not plugins:
        for m in models:
            globals()[m.__name__] = m
    else:
        for m in models:
            for p in plugins:
                if m.__name__.lower() == p.lower():
                    pass
