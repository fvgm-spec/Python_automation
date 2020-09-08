#!/usr/bin/env python3

import re
def find_user_log(text):
	pattern = r"USER \((\w+)\)$"
	result = re.search(pattern, text)
	return result[1]

print(find_user_log("Computer.name CRON[29440]: USER (good_user)"))
#computer.name jam_tag=psim[29187]: USER (UUID:006)
#computer.name jam_tag=psim[29187]: USER (UUID:007)
#computer.name CRON[29440]: USER (naughty_user)
#computer.name cacheclient[29807]: start syncin
#computer.name CRON[29440]: USER (naughty_user)
#computer.name CRON[29440]: USER (naughty_user)


