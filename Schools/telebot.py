 token = '406079095:AAFGXvER3fWbiT08kXKzMyvcylmjS_eVMIs'
    bot = telebot.TeleBot(token)

    config_file = open('/opt/telebot/config.json','r')
    config = json.load(config_file)
    config_file.close()

    def extract_from_config(name):
        try:
            return set(config[name])
        except Exception as ex:
            print('Error: {0}'.format(ex))
            return set()


    allowed_users = extract_from_config('allowed_users')
    allowed_chats = extract_from_config('allowed_chats')

    def dump_object(obj):
      return json.dumps(obj,
           default=lambda o: o.__dict__)

    def dump_object_pretty(obj):
      return json.dumps(obj, indent=4,
           default=lambda o: o.__dict__)

    def check_and_run(src_command, arguments):
        command = list()
        if type(src_command) is list:
           command.extend(src_command)
        elif type(src_command) is str:
           command.extend([src_command])
        else:
           #exit from application on format errors
           sys.exit(-1)

        command.extend(arguments)
        print("Run command {0}\n".format(command))
        with subprocess.Popen(' '.join(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as proc:
           return proc.stdout.read().decode('utf-8'), proc.stderr.read().decode('utf-8')


    def command_config(arguments):
        command = [ '/bin/bash','/usr/local/rancid/scripts/School/Switch_SCH/config_school_bot.sh' ]
        return check_and_run(command, arguments)

    def command_printf(arguments):
        command = [ '/usr/bin/printf']
        return check_and_run(command, arguments)

    def command_ls(arguments):
        command = [ '/bin/ls']
        return check_and_run(command, arguments)

    def command_find(arguments):
        command = [ '/bin/bash','/usr/local/rancid/scripts/School/find/find.sh' ]
        return check_and_run(command, arguments)

    def command_help(arguments):
        command = [ '/bin/cat','/opt/telebot/help.txt' ]
        return check_and_run(command, arguments)

    def command_conn(arguments):
        command = [ '/bin/bash','/usr/local/rancid/scripts/School/find/conn.sh' ]
        return check_and_run(command, arguments)

    def command_done(arguments):
        command = [ '/bin/bash','/usr/local/rancid/scripts/School/done/done.sh' ]
        return check_and_run(command, arguments)

    def command_ap_status(arguments):
        command = [ '/bin/bash','/usr/local/rancid/scripts/School/ap-status/ap-status_test.sh' ]
        return check_and_run(command, arguments)

    def send_message(telegram_message, string):
        if len(string) > 5500:
            with io.StringIO('\n'.join([telegram_message.text, string])) as file:
                bot.send_document(telegram_message.chat.id, file)
        else:
            bot.reply_to(telegram_message, string)

    def on_message(message):
       # limit content type
       if message.content_type != 'text':
          bot.reply_to(message, 'Content-type must be text')

       user = message.from_user
       chat = message.chat
       text = message.text

       user_allowed = (user.id in allowed_users)
       chat_allowed = (chat.id in allowed_chats)

       # chedk user existence
       if not user_allowed and not chat_allowed:
            answer = ''
            if not chat_allowed and message.chat.id != message.from_user.id:
                answer = '{0} messages from chat {1} have no permissions to run tasks.'.format(answer, dump_object(chat))
            if not user_allowed:
                answer = '{0} user {1} have no permissions to run tasks'.format(answer, dump_object(user))
            bot.reply_to(message, answer)
            return

       command_splited = text.split(' ')
       command = command_splited[0]
       arguments = command_splited[1:]
       stdout = ''
       stderr = ''
       if command == '/config':
           stdout, stderr = command_config(arguments)
           #bot.reply_to(message, 'Job done'.format(command))
       elif command == '/printf':
           stdout, stderr = command_printf(arguments)
           #bot.reply_to(message, 'Job done'.format(command))
       elif command == '/ls':
           stdout, stderr = command_ls(arguments)
       elif command == '/find':
           stdout, stderr = command_find(arguments)
           #bot.reply_to(message, 'Job done'.format(command))
       elif command == '/help':
           stdout, stderr = command_help(arguments)
       elif command == '/start':
           stdout, stderr = command_help(arguments)
       elif command == '/conn':
           stdout, stderr = command_conn(arguments)
           #bot.reply_to(message, 'Job done'.format(command))
       elif command == '/wlc-ap':
           #stdout, stderr = command_wlc_ap(arguments)
           bot.reply_to(message, 'Command deprecated. Use /ap-status *'.format(command))
       elif command == '/wlc-cfg':
           #stdout, stderr = command_wlc_cfg(arguments)
           bot.reply_to(message, 'Command deprecated. Use /help *'.format(command))
       elif command == '/done':
           stdout, stderr = command_done(arguments)
           #bot.reply_to(message, 'Job done'.format(command))
       elif command == '/ap-status':
           stdout, stderr = command_ap_status(arguments)
           #bot.reply_to(message, 'Job done'.format(command))
       else:
           bot.reply_to(message, 'Unknown command {0} '.format(command))
           return

       if len(stdout) != 0:
           print(stdout)
           send_message(message,stdout)
           #bot.reply_to(message, stdout)

       if len(stderr) != 0:
           err = 'Error: \n' + stderr
           send_message(message,err)
           #bot.reply_to(message, err)

       #print(dump_object_pretty(message))

    def main_handler(messages):
        for m in messages:
            on_message(m)

    bot.set_update_listener(main_handler)
    bot.polling(none_stop = True)

if __name__ == '__main__':
   run()