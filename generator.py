class Openings:
    
    jobs = {'1152364' : ['Java & UI Developer', 'West Des Moines, IA', 'Sammons Financial Group'], '1152261': ['Java Developer with Angular', 'Boston, MA', 'Fidelity Investments'], '1151997' : ['Java Developer', 'Tulsa, OK', 'Change Health Corporation'], '1151723': ['Fullstack Java Developer', 'Eden Prairie, MN', 'Lifetouch']}

    def listjob(self):
        for key, value in self.jobs.items():
            self.eid = key
            self.title = value[0]
            self.location = value[1]
            self.company = value[2]
            print('Job Listing ' + str(key) + ': ' + str(value[0]) + 'located in ' + str(value[1]) + ' working for ' + str(value[2]) + '. Apply today if you are interested!')

shoutout = Openings()
shoutout.listjob()

# Work with a recruiter who will understand you
# Richard Eby aka The Coding Recruiter
