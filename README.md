# Portfolio Built with Django

This repository contains the code for my personal portfolio website built using Django, a high-level Python web framework. This portfolio showcases my projects, skills, and experiences in a clean and organized manner.

## Features

- **Project Showcase**: Display your projects with details such as descriptions, technologies used, and links to the code repository or live demo.
- **Skills**: Highlight your skills and expertise in various technologies, tools, and programming languages.
- **Experience**: Present your professional experience, education, and certifications.
- **Contact**: Provide a way for visitors to get in touch with you via a contact form or links to your social media profiles.

## Setup Instructions

1. **Clone the Repository**:
```
git clone <repository-url>
```


2. **Create a Virtual Environment** (Optional but recommended):
```
python3 -m venv env
```


3. **Activate the Virtual Environment**:
- On Windows:
  ```
  env\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source env/bin/activate
  ```

4. **Install Dependencies**:
```
pip install -r requirements.txt
```


5. **Database Setup**:
- By default, this project uses SQLite for development. You can change the database settings in `backend/settings.py` if needed.
- Run migrations to create database tables:
  ```
  python manage.py migrate
  ```

6. **Create a Superuser** (Admin):
```
python manage.py createsuperuser
```


7. **Run the Development Server**:
```
python manage.py runserver
```


8. **Access the Website**:
Open your web browser and go to `http://localhost:8000` to view your portfolio website.

## Customization

- **Content**: Update the content of your portfolio by modifying the templates and static files in the `portfolio` app.
- **Styling**: Customize the appearance of your portfolio by editing the CSS files in the `static` directory.
- **Database Models**: Modify the database models in the `models.py` file to suit your needs.
- **Admin Panel**: Access the Django admin panel at `http://localhost:8000/admin` to manage your projects, skills, experiences, and other content.

## Deployment

- **Heroku**: Deploy your Django portfolio on Heroku following the instructions provided in the [Heroku Django documentation](https://devcenter.heroku.com/articles/deploying-python).
- **Other Platforms**: You can deploy your portfolio on other platforms like AWS, DigitalOcean, or PythonAnywhere by configuring the server environment and uploading your code.

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
