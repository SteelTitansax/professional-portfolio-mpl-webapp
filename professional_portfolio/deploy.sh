az webapp up --name manuel-portero-professional-website --resource-group rg-spaincentral-portfolio-mpl --runtime "PYTHON:3.9"
# startup command
# gunicorn --workers 3 --bind 0.0.0.0:8000 professional_portfolio.wsgi:application
# Use this comand before deploy the app, for preparing the static files. 
# python manage.py collectstatic
