# Behind the Scenes of Stardom: Decoding the Patterns in Actors' Careers  <img src="Data/Images/LinkedIn_logo_initials.png" alt="LinkedIn Logo" width="25" height="25">

## Abstract
How do you envision your career? We, as scientists, will probably spend a substantial portion of our career in the same company in a specific field, like pharma, robotics or data science for the most talented of us. For actors, the journey is more complex, involving potential shifts between diverse movie genres and marked by the inevitable highs and lows inherent to the profession. In our project, we aim at analyzing the trajectory of acting careers. 

Usually, when you seek information about someone's career, you turn to LinkedIn. Would you do the same to stalk your childhood actor crush? Well, good news, we are here to do it for you. From the number of connections (actors they have collaborated with), to the potential genre specialization in movies, and not forgetting the prospect of winning an Oscar, let’s delve into the intricacies of our actors’ careers. 

## Research Questions

1.	What characterize the career evolution of actors?
2.	How do actors navigate and evolve through different genres over the course of their career? 
3.	Are successful actors more interconnected between each other than to other actors? A REFAIRE
4.	What shared attributes distinguish actors who have received Oscar nominations?

## Additional Datasets 

- [**IMDb Datasets**](https://www.imdb.com/interfaces/) - We incorporated two IMDb datasets, namely `title.basics` and `title.ratings`, into our analysis to extract movie ratings. These datasets will be used to uncover correlations between actors' careers and the ratings of the movies they participate in. The information includes average ratings and the number of votes from a vast database of 10 million movies. Upon merging with our [**CMU Movie Summary Corpus**](http://www.cs.cmu.edu/~ark/personas/), we achieved a matching rate of 62%.

- [**Oscars**](https://www.kaggle.com/datasets/unanimad/the-oscar-award) - The Oscars dataset, sourced from Kaggle and scraped from the Official Academy Awards site, spans nominations from $1927$ to $2022$ across various categories. For our analysis, we retain categories related to actors.

## Methods

0. Merging the datasets

The first step of our analysis is to merge the different datasets we are using. As they are not sourced from the same database, they don't have a common unique identifier. Therefore, we had no choice but to merge on names of either of movies or actors. This pose an issue as if a title can be written in different formats and the matching might not be exact. For example, the title 'Harry Potter and the Deathly Hallows Part I' can also be written as 'Harry Potter and the Deathly Hallows Part 1'. In this case the standard matching will not work. To resolve this problem we first standardize the titles by removing special characters and setting all the characters to lower case. We then used Fuzzy Matching using the `rapidfuzz` library in order to match the movie titles that are sufficiently close to eachother using the WRatio similarity metric. We can then perform the merge on the matched titles and release year. 

1. Career characterization

... blabla jennifer

2. Genres exploration

To explore how actors transition across various genres, our initial step involves unifying genre information from both the [CMU](http://www.cs.cmu.edu/~ark/personas/) and [IMDb](https://www.imdb.com/interfaces/) datasets. Initially, we combine genres and then standardize them. The combined dataset yields over 300 unique genres, making it impractical for analysis. To tackle this issue, we conduct a frequency analysis, identifying the most common words associated with genres. This process results in a refined set of 26 main genres.

Next, we examine movies genres from an actor-centric perspective. By examining the number of movies each actor participated in within each genre, we obtained a distribution of movies for each actor across diverse genres. With this information, we inferred correlations between the proportions of movies associated with pairs of genres. Employing the Pearson correlation coefficient and its associated p-value facilitated this correlation analysis. The Pearson correlation coefficient and its associated p-value was used for that part. 

Moving forward to Milestone P3, our objective is to delve into how actors evolve across different genres. To accomplish this, we plan to construct a Markov Chain, with each state representing a distinct genre and the edges indicating the probabilities of transitioning from one genre to another. Additionally, we aim to integrate genres into our network analysis to observe potential clustering patterns among actors.

3. Network Analysis



4. Ethnicities and Oscars

## Proposed timeline

```
.
│  
├── 18.11.22 - Pause project work
│  
├── 01.12.22 - Homework 2 deadline
│  
├── 03.12.22 - Update according to P2 feedback 
│    
├── 05.12.22 - Construct genres Markov chain 
│  
├── 09.12.22 - Construct complete actor network 
│  
├── 12.12.22 - Finalize analysis
│   
├── 14.12.22 - Finalize notebook P3
│  
├── 15.12.22 - Begin data story
│  
├── 21.12.22 - Finish data story
│  
├── 22.12.22 - Update README
│  
├── 22.12.22 - Milestone 3 deadline
│ 
.
```

## Organization within the team

- Michael Ha : Merging the datasets
- Jennifer Abou-Najm : Career characterization
- Valérie Costa : Genres exploration
- Mariem Boughzala :  Network Analysis
- Adrien Vannson : Ethnicities and Oscars

## Questions for TAs



