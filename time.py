import time, datetime, vk_api, os

def main():
    token = os.environ.get('token')
    vk_session = vk_api.VkApi(token=str(token))

    try:
        def countdown(stop):
            while True:
                difference = stop - datetime.datetime.now()
                count_hours, rem = divmod(difference.seconds, 3600)
                count_minutes, count_seconds = divmod(rem, 60)
                if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
                    print("end")
                    break
                #vk_session.auth()
                #vk_session.method("status.set",f"{str(difference.days)}:{str(count_hours)}:{str(count_minutes)}:{str(count_seconds)}")
                vk_session.method("status.set",{"text":f"{str(difference.days)}:{str(count_hours)}:{str(count_minutes)}:{str(count_seconds)}"})
                time.sleep(30)


        end_time = datetime.datetime(2019, 11, 1, 0, 0, 0)
        countdown(end_time)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
main()
