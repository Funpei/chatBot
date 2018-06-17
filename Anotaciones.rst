
The downgrade to html5lib 1.0b8 in @Bhavuk answer works but courses a version issue with bleach.

The solution for me was with a change of version of bleach to be compatible with the new version of html5lib

pip3 install --upgrade bs4
pip3 install --upgrade bleach==1.4.2
pip3 install --upgrade html5lib==1.0b8