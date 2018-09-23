import re

pattern = r'https://github.com/(?P<username>([a-zA-Z]+\d)*)+/(?P<reponame>([a-zA-Z]+\d*)+)+\.git'
f = open("2.txt")
name_pattern = r"[A-Za-z0-9_-]+"
re_pattern = r"https://github.com/(?P<username>%s)/(?P<repo>%s).git" %(name_pattern,name_pattern)
p = re.compile(re_pattern)
for line in f:
    print(re.fullmatch(re_pattern, 'https://github.com/Ya/repo1.git'))


s2_pattern = "git@github.com:%s/%s.git"

#ssh_path = s2_pattern %(m.group("username"), m.group("repo"))