y="      - name: checkout XXX2024
        uses: actions/checkout@v4
        with:
          repository: orgpedia/XXX2024
          path: import/XXX2024
          sparse-checkout: |
            export/orgpedia_XXX2024"

for f in `echo $MAH_DEPTS`; 
do 
    echo "$y" | sed "s/XXX/$f/";
    echo;
done
