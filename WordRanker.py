from yaspin import yaspin       #used for loading icon
from tabulate import tabulate   #used for pretty table
import wikipediaapi             #used to grab wikipedia arcticle (slices section in debug mode)
from collections import Counter #used to count array of words. 


@yaspin(text="Fetching table data...")
#Scrapes the words from wiki page
def fetchWords():
    wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.HTML
 )

    wikipage = wiki.page('Microsoft')
    results = str(wikipage.section_by_title('History').full_text)  #this will cut short in debug mode. 
    #print(results)
    return results

def rankWords(tableData,NumberOfRows,BlacklistWords):
    wordArray = tableData.split(' ')
    blacklist = BlacklistWords.split(',')
    for word in wordArray:
        if word in blacklist:
            wordArray.remove(word)

    wordlist =Counter(wordArray).most_common(NumberOfRows)

    return wordlist

def main(
  Welcome: str = print("Welcome to WordRanker."),
  NumberOfRows: int = input('Please enter # of rows: '),
  BlacklistPrompt: str = print("Please add any words you'd like to blacklist, seperated by a , \n Ex. Bing,Bill"),
  BlacklistWords: str = input("BlacklistWords: ")
):
  NumberOfRows = int(NumberOfRows)
  tableData=fetchWords()
  tableRank=rankWords(tableData,NumberOfRows,BlacklistWords)
  ##Now print the table data with tabulate as below
  headers = ["Word", "# of Occurrences"]
  print(tabulate(tableRank, headers, tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()