from datetime import datetime

LOG_FORMAT = "[%(asctime)s]-{%(pathname)s:%(lineno)d}-{%(levelname)s}-{In file ->%(module)s " \
             "In function ->%(funcName)s}-{%(message)s}"

dt_time=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
now_time=datetime.now()

q_address_input="""select * from address_input where needs_lookup=1;"""
