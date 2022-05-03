# Django-Bootstrap Blogging Template Pro

This is a **Free**, **Production grade**, django-bootstrap blogging template along with **Personal Portfolio**. It consist of various unique features mentioned below.

>**NOTE: I'll continuously be updating this template and add new features, make sure you fork it and in case you like it, please don't forget to leave a STAR**!

The **LIVE VERSION** of this website can be seen here: 
>**Blog**: https://thefortyseven.dev  
**Portfolio**: https://thefortyseven.dev/portfolio

# Features:
Complete List of Features:
- Responsive and Minimal Design 
- Latest Bootstrap 5 and Django 4
- Secret /admin URL (define your own URL for admin login page)
- REST API based user Login and Signup
- Group based user access
- reCaptcha Integrated  Login/Signup Page
- Cookie Consent box
- Blog based Unique IP based view count 
- Email based user account verification
- Email based user password reset option
- Editable User Profile
- Froala Editor for writing blogs
- Search Blogs and Users
- Most Viewed Blogs and Recently Updated Blogs section
- Preview Blog before sending for approval
- User Types: 
	- **Superuser** 
		- Edit/Delete any blog from ANY user .
		- Approve a blog and make it live.
		- Manage user account (Block any user account, Change Password, Edit User Profile Data).
		- Resend Verification Email.
		- View Contact Messages.
		- Manage Subscriptions .
	- **Staff**
		- Create/Edit/Delete own blogs.
		- See a List of own blogs along with it's Publish Date and Total Views in 'My Blogs' section.
	- **Viewer** 
		- Comment on any blog
- AWS Deployment Ready
- About, Legal, Contact, Donate Pages
- Sensitive Credentials are stored as ENV variables


# Services - Technologies Used:
The technologies used are listed below:
- Frontend: Bootstrap
- Backend: Django
- Database: PostgreSQL

The technologies used are listed below:
- Server: Apache
- Hosted on: AWS EC2
- Email SMTP: AWS SES
- Static Content: AWS S3
- Database: AWS RDS Postgres and Local
- SSL: Free SSL from CertBot Integrated


# Defaults:
By default, 
- A user created through signup page is a **Viewer** user type.
- A blog needs to be sent for review so as to get an approval and make it live, until then it sits in the user profile only.
- Editing a blog will take it down from live and it needs an approval again.
- Search Bar will query through Blog Titles and Users FirstName, LastName. 


# Set ENV Variables
You'll have to declare all the secret credentials in an `.env` file in the project folder.

```
#=========== DJANGO APP CONFIG ===========
ADMIN_URL = <ANY NAME TO ACCESS THE /ADMIN PAGE EX: secret>
SECRET_KEY = <DJANGO SECRET KEY>
DEBUG = True
ALLOWED_HOSTS = 'YOURDOMAIN.COM, 127.0.0.1'
CSRF_TRUSTED_ORIGINS = 'https://YOURDOMAIN.COM, http://127.0.0.1'

#============== SET TO True IN PRODUCTION =============
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_SSL_REDIRECT = False
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_SECONDS = 3600

#=========== GOOGLE CAPTCHA CONFIG ===========

GOOGLE_RECAPTCHA_SITE_KEY = <RECAPTCHA SITE KEY>
GOOGLE_RECAPTCHA_SECRET_KEY = <RECAPTCHA SECRET KEY>


#=========== EMAIL CONFIG ===========

EMAIL_FROM_VERIFY = VERIFY <verify@YOURDOMAIN.COM>
EMAIL_FROM_RESET = RESET <reset@YOURDOMAIN.COM>


EMAIL_MAIL_SUBJECT = Confirm Your Email
EMAIL_MAIL_HTML = verification-email.html
EMAIL_MAIL_PLAIN = mail_body.txt
EMAIL_TOKEN_LIFE = 3600
EMAIL_PAGE_TEMPLATE = email-confirmation.html
EMAIL_PAGE_DOMAIN = https://YOURDOMAIN.COM
EMAIL_MULTI_USER = True
EMAIL_HOST = email-smtp.<SES HOST LOCATION>.amazonaws.com
EMAIL_PORT = 587
EMAIL_HOST_USER = <AWS SES USER NAME>
EMAIL_HOST_PASSWORD = <AWS SES USER PASSWORD>
EMAIL_USE_TLS = True


#=========== AWS POSTGRES RDS DATABASE CONFIG ===========

DB_ENGINE = django.db.backends.postgresql
DB_NAME = <DB NAME>
DB_USER = <POSTGRES USERNAME>
DB_PASSWORD = <USER PASSWORD>
DB_HOST = <POSTGRES HOST NAME>
DB_PORT = 5432

#=========== AWS S3 CONFIG ===========

AWS_ACCESS_KEY_ID = <AWS ACCESS ID>
AWS_SECRET_ACCESS_KEY = <AWS SECRET KEY>
AWS_STORAGE_BUCKET_NAME = <AWS S3 BUCKET NAME>
AWS_S3_FILE_OVERWRITE = False
DEFAULT_FILE_STORAGE = storages.backends.s3boto3.S3Boto3Storage
STATICFILES_STORAGE = storages.backends.s3boto3.S3StaticStorage
AWS_S3_ENDPOINT_URL = https://s3-accelerate.amazonaws.com
AWS_S3_SIGNATURE_VERSION = s3v4
AWS_S3_REGION_NAME = <AWS S3 REGION>
```



# Screenshots:
### HOMEPAGE
![HOMEPAGE](screenshots/homepage.jpg)

### LOGIN
![LOGIN](screenshots/login.jpg)

### SIGNUP
![SIGNUP](screenshots/signup.jpg)

### MY BLOGS
![MYBLOGS](screenshots/myblogs.jpg)

### APPROVAL PAGE
![APPROVALPAGE](screenshots/forapproval.jpg)

### ACTIVATE USER
![ACTIVATEUSER](screenshots/activateuser.jpg)
