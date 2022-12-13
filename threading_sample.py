import urllib.request, time, threading

def get_docu(page):
    print('wikidocs page:{}'.format(page))
    resource = 'https://wikidocs.net/{}'.format(page)

    try:
        with urllib.request.urlopen(resource) as s:
            with open('wikidocs_%s.html' % page, 'wb') as f:
                f.write(s.read())
    except urllib.error.HTTPError:
        return 'Not Found'

start = time.time()

pages = [12,13,14,15]
threads = []


#for page in pages:
#    get_docu(page)

#thread를 사용하여 병렬적으로 처리
for page in pages:
    t = threading.Thread(target=get_docu, args=(page,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print('수행시간: %f 초' %(end-start))