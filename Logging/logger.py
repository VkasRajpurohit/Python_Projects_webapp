import logging as lg

# Create and configure logger
lg.basicConfig(filename="PythonProjects_webapp/Logs/logfile.log",
               filemode='w',
               level=lg.INFO,
               format='%(asctime)s %(levelname)s: %(message)s',
               datefmt='%Y-%m-%d %H:%M:%S')


