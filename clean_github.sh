while read r;
  do 
    curl -XDELETE -H 'Authorization: token {token}' "https://api.github.com/repos/$r ";
done < repos.txt
