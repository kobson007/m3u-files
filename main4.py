import time
from github import Github
from git import Repo
import os

# მახასიათებლები
FILE_PATH = '/home/kali/Desktop/m3u-files/geo.m3u'  # m3u ფაილის სრული გზა
REPO_PATH = '/home/kali/Desktop/m3u-files'  # GitHub რეპოზიტორიის ადგილმდებარეობა
GITHUB_TOKEN = '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'  # GitHub ტოკენი
GITHUB_REPO_NAME = 'kobson007/m3u-files'  # GitHub რეპოზიტორიის სახელი

# GitHub რეპოზიტორიის კავშირი
def connect_github():
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(GITHUB_REPO_NAME)
    return repo

# m3u ფაილის განახლება (შეავსეთ თქვენი ლოგიკა)
def update_m3u_file():
    # აქ უნდა იყოს თქვენი ლოგიკა ტოკენის განახლებისთვის და მ3უ ფაილის განახლებისთვის
    token = get_new_token()  # ამოიღეთ ახალი ტოკენი
    with open(FILE_PATH, 'w') as f:
        f.write(f'https://tbs01-edge32.itdc.ge/{token}.m3u8')  # ახალი m3u ფაილის დაწერა

# ახალი ტოკენის მიღება (ინტეგრაცია უნდა გავაკეთოთ თქვენი ტოკენის ძიებისთვის)
def get_new_token():
    # ეს ადგილი უნდა შეიცვალოს თქვენს API ან ტოკენის აღების ლოგიკაზე
    return 'new_generated_token'  # დააბრუნეთ ახალი ტოკენი

# GitHub-ზე ფაილის ატვირთვა
def upload_to_github():
    repo = Repo(REPO_PATH)  # რეპოზიტორიის კავშირი
    repo.index.add([FILE_PATH])  # ფაილის დამატება
    repo.index.commit('Auto-update m3u file')  # კომიტი
    origin = repo.remotes.origin
    origin.push()  # განახლების ატვირთვა GitHub-ზე

# ავტომატური განახლება
def auto_update():
    while True:
        update_m3u_file()  # მ3უ ფაილის განახლება
        upload_to_github()  # ატვირთვა GitHub-ზე
        print("m3u file updated and uploaded to GitHub.")
        time.sleep(60 * 5)  # ყოველ 5 წუთში განახლება (ან თქვენი საჭიროების მიხედვით)

# მთავარი ფუნქცია
if __name__ == '__main__':
    auto_update()  # სკრიპტის გაშვება
