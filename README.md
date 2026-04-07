# BetterEncryptV2
password generator that balances security and memorabillity 

replace postgresql database login info and django security key.

***Requires vaild Hugging Face token (all permisons)***

## Local setup (Django)

From `betterencryptv2/`:

- Create virtualenv and install deps:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

- Configure environment:
  - Copy `betterencryptv2/.env.example` to `betterencryptv2/.env`
  - Set `DJANGO_SECRET_KEY`
  - Optional: set `HF_TOKEN` to enable the Hugging Face prompt-to-(security,memorability) flow
  - Optional: set `POSTGRES_*` variables if you want Postgres; otherwise sqlite is used by default.

- Run migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

- Run tests:

```bash
python manage.py test
```