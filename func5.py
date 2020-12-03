def ask_ok(prompt, retries=4, reminder='Please try again!'):
    """
    this functions gets a prompt from the user and checks if input is yes/no
    :param prompt:
    :param retries:
    :param reminder:
    :return:
    """
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok("Hey, Please enter Yes or No:\n",retries=3)