from threading import Thread

from flask import current_app, render_template, app

from app import mail
from flask_mail import Message


def send_asyn_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            raise e


def send_mail(to, subject, template, **kwargs):
    # python email
    msg = Message('[鱼书]' + ' ' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=send_asyn_email, args=[app, msg])
    thr.start()
    # mail.send(msg)
