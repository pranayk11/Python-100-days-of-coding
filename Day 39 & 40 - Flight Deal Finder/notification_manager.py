import smtplib

MY_EMAIL = "herta.yundt96@ethereal.email"
MY_PASSWORD = "zbc8QtJ3E6rmf54RPe"


class NotificationManager:

    def send_mail(self, message, google_flight_link):
        with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
