from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app, session, render_template_string
# ... the rest of your imports
from flask_login import login_required, current_user
from .models import EmailUser
from flask_mail import Mail, Message
from . import db, Mail, mail



views = Blueprint('views', __name__)

@views.route('/ebook', methods=['GET', 'POST'])
def ebookPage():
    email = request.form.get('email')
    name = request.form.get('name')
    print(name)


    # if not email:
    #     # flash('No email provided')
    #     return render_template('404.html')

    if email and name:
        existing_user = EmailUser.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists.')
            return render_template('ebook.html')
        else:
            new_email_user = EmailUser(email=email, name=name)

            topic = "It is time you finally take action"
                    
            htmlEBOOK = render_template_string("""
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            background-color: #ffffff;
            width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .message {
            font-size: 16px;
            line-height: 1.6;
            color: #333333;
        }
        .footer {
            font-size: 12px;
            color: #777777;
            margin-top: 20px;
            text-align: center;
        }
        .download-button {
            display: inline-block;
            padding: 10px 15px;
            margin-top: 20px;
            background-color: #007bff;
            color: #ffffff;
            text-decoration: none;
            border-radius: 5px;
        }
    </style>
</head>


<head>
<style>
  body {
    font-family: Arial, sans-serif;
    color: #333;
    line-height: 1.6;
  }

  .email-link {
    color: #3498DB;
    text-decoration: none;
    font-weight: bold;
  }
</style>
</head>
<body>

<p>Hi there {{ name }},</p>

<p>For too long you have procrastinated,</p>

<strong><u><p class="highlight">It is finally time to change that.</p></u></strong>

<p>This ebook is your first step to achieving success.</p>

<p>In addition to that,</p>

<p>You will also receive <strong><u>weekly emails </u></strong> from me.</p>

<p>These emails will be packed with everything I know.</p>

<p>Money. Gym. Masculinity. Discipline.</p>

<p>All of that you get for completely free...</p>


<u><p>This is the <span class="highlight">opportunity of your life,</u></span></p>

<p>If you put in the work,</p>

<p><strong><u><span class="highlight">There is no way for you to fail</span></p> </strong> </u>

  <p><a href="/download/59853959457" class="email-link">👉==Click here to get the ebook==</a></p>

<p>Thank you for signing up</p>

<p>-Mindvate</p>

</body>
</html>

""", name=name)
            msg = Message(topic, recipients=[email], html=htmlEBOOK, sender=("Mindivate", "email@mindivate.com"))
            mail.send(msg)
            db.session.add(new_email_user)
            db.session.commit()
            return render_template('gotEbook.html', email=email, name=name)

    return render_template('ebook.html')


@views.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@views.route('/test', methods=['GET', 'POST'])
def test():
    return("<h1>test</h1>")



@views.route('/email/ejnfsjf4348f43njfdj94b34j3', methods=['GET', "POST"])

def email():
    # if not current_user.is_authenticated:  # Add this line to check if the user is not logged in
    #     return redirect(url_for('login'))
   
    all_emails = [user.email for user in EmailUser.query.all()]
    all_names = [userName.name for userName in EmailUser.query.all()]
    
    all_users = EmailUser.query.all()

    topic = request.form.get('topic')
    message = request.form.get('message')
    if request.method == 'POST': 

        msg = Message()





#email sending 


        all_users = EmailUser.query.all()
        nameAdd = request.form.get('nameAdd')
        individual_message = ""
        confirm_button = request.form.get('submit')
        test_button = request.form.get('test_submit')

        if True:

            if nameAdd != None:
                    
            
                for user in all_users:
                    all_users = EmailUser.query.all()
                    formatted_message = request.form.get('message')
                    combined_message = f"<p>Hi {user.name}!\n\n</p>{formatted_message}"
                      # Add this line to obtain the formatted text
                    msg.body = f'Hi {user.name}!\n\n{message}'
                    msg = Message(topic, recipients=[user.email], html=combined_message)  # Include the formatted text in the email message
                    
                    message = ("To: " + user.email + "\nDear " + user.name + "\nTOPIC: " + topic + "\n" + message)
                    html_content = """
        <html>
        <head>

        </head>
        <body>

    {{message}}
        </body>
        </html>
        """
                mail.send(msg)
                return redirect('/ebook')
            
                
            else:
                for user in all_users:
                    all_users = EmailUser.query.all()
                    formatted_message = request.form.get('message')  # Add this line to obtain the formatted text
                    msg.body = f'Hi {user.name}!\n\n{message}'
                    
                    msg = Message(topic, recipients=[user.email], html=formatted_message)  # Include the formatted text in the email message
                    
                    message = ("To: " + user.email + "\nDear " + user.name + "\nTOPIC: " + topic + "\n" + message)
                    html_content = """
        <html>
        <head>

        </head>
        <body>

    {{message}}
        </body>
        </html>
        """    
                mail.send(msg)
                return redirect('/sent')     
    
            

        
  

        
    return render_template('email.html', all_emails=all_emails, message=message, all_users=all_users)


@views.route('/file')
def download_file():
    return current_app.send_static_file('demofile2.txt')

@login_required
@views.route('/sent')
def sent():
    return render_template('getEbook.html')




@views.route('/')
def home():
    return redirect('/ebook')

from flask import send_from_directory

@views.route('/download/59853959457')
def download_ebook():
    # Define the directory where your eBooks are stored
    ebook_directory = 'ebook'
    
    # Define the filename based on ebook_id, assuming it's a direct mapping
    # For instance, if ebook_id = '234453', the filename might be 'ebook_234453.pdf'
    ebook_filename = '7_BEST_Productivity_Techniques.pdf'

    # Send file from directory
    return send_from_directory(ebook_directory, ebook_filename, as_attachment=True)
