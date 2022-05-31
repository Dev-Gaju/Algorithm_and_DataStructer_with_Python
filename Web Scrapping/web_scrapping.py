import time

from bs4 import  BeautifulSoup
import requests

print("Put some skill you are not familiar with")
unfamiliar_skills = input('>')
print("filtering Out", unfamiliar_skills)

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Machine+Learning&txtLocation=').text #only text
    # print(html_text)

    soup = BeautifulSoup(html_text, 'lxml')
    # jobs = soup.find_all('li', class_ ='clearfix job-bx wht-shd-bx')
    jobs = soup.find_all('li', class_ ='clearfix job-bx wht-shd-bx')
    # print(jobs)
    # for job in jobs:
    for index, job in enumerate (jobs):   #when save into text file
        days_arrive = job.find('span', class_='sim-posted').text
        if 'few' in days_arrive:
            company_name = job.find('h3', class_= 'joblist-comp-name').text.replace(' ', '') #company_name
            # print(company_name)
            skill_requirement = job .find('span', class_ ='srp-skills').text.replace(' ','')
            job_info = job.header.h2.a['href']
            if unfamiliar_skills not in skill_requirement:
            # print(skill_requirment)
            #alt + shift for multiple word edit
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company_name : {company_name.strip()}\n')
                    f.write(f'Request_skills: {skill_requirement.strip()}\n')
                    f.write(f'More info {job_info}')
                print("file save: ", index)
                    # print(f'Company_name : {company_name.strip()}')
                    # print(f'Request_skills: {skill_requirement.strip()}')
                    # print('More info', job_info)

if __name__ =='__main__':
    while True:
        find_jobs()
        time_wait = 10
        print('Waiting', time_wait, 'Minutes...')
        time.sleep(time_wait * 60)









# print(days_arrive)
#         print(f'''
#         Company_name  =  {company_name}
#         Request_skills =  {skill_requirement}
#         Published date = { days_arrive}
#         ''')