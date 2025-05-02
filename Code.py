Configuring remote repository:

*Ganyan dapat itsura ng start niya >> GWEN TEVEZ@DESKTOP-MT65BM6 MINGW64 ~

cd /c
cd repo
ssh-keygen -t ed25519 -C "tevesgwenn.sch@gmail.com"
Enter
Create passkey
Re enter passkey


*Ganto na dapat itsura ng sunod >> GWEN TEVEZ@DESKTOP-MT65BM6 MINGW64 /c/repo (main)

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
Enter passphrase 
clip < ~/.ssh/id_ed25519.pub 


*by that, maca-copy mo yung ssh public key mo parang ganito itsura "SHA256:uPB0G0hsiNME5VYMMRHvgCyZvg1stFjSt+OnMDjcOCs"

*Punta ka na sa github mo

Click profile photo
Click settings
Sa access section sidebar, click SSH and GPG keys.
Click new ssh key
Add title >> "Personal Laptop"
Magpaste ka sa key
Click add SSH key


*Punta ka na sa page 32 ng ppt ni sir. Option 2 yung susundan natin.

Upload images:

cd /c

*kunin yung url sa "<>Code" dropdown arrow, click ssh
git clone git@github.com:PUP-BSIT/exercise-1-and-2-teves-gwen.git
yes
passkey
cd exercise-1-and-2-teves-gwen
git status
git remote -v
mv "/c/Users/GWEN TEVEZ/Downloads/teves_gwen_exercise_1.jpg" .
git status
git add teves_gwen_exercise_1.jpg
git status
mv "/c/Users/GWEN TEVEZ/Downloads/teves_gwen_exercise_2.jpg" .
git add teves_gwen_exercise_2.jpg
git status

*dapat naka add na yung 2 file (green na)

git commit -m "Add exercise 1 and 2 scores."
git push origin main 
passkey


Upload screenshots:

mkdir Screenshots
cd Screenshots
mv "C:\Users\GWEN TEVEZ\Downloads\Screenshot1.png" .
mv "C:\Users\GWEN TEVEZ\Downloads\Screenshot2.png" .
git add Screenshot1.png
git add Screenshot2.png
git status (just to check if the file is now existing)
git commit -m "Add screenshots."
git push origin main 
passkey


Remove directory:
git rm -r Screenshots
git commit -m "Remove directory."
git push origin main
passkey


Remove file:
git rm teves_gwen_exercise_1.jpg
git commit -m "Remove file."
git push origin main
passkey
okay na po hehe


Remove clone:
rm -rf exercise-1-and-2-teves-gwen
ls
restart 
