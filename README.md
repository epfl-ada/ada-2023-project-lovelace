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

- [**Freebase dataset**](https://developers.google.com/freebase) - Full archive of the Freebase database. The archive is used to convert Freebase IDs to text strings. Processing the data took a rather long time and had to be done carefully since the the dataset has an important size: more than 30 Go compressed.

## Methods

0. Merging the datasets

The first step of our analysis is to merge the different datasets we are using. As they are not sourced from the same database, they don't have a common unique identifier. Therefore, we had no choice but to merge on names of either movies or actors. This poses an issue, as a title can be written in different formats, and the matching might not be exact. For example, the title 'Harry Potter and the Deathly Hallows Part I' can also be written as 'Harry Potter and the Deathly Hallows Part 1'. In this case, the standard matching will not work. To resolve this problem, we first standardize the titles by removing special characters and setting all the characters to lowercase. We then use Fuzzy Matching with the `rapidfuzz` library to match movie titles that are sufficiently close to each other using the WRatio similarity metric. We can then perform the merge on the matched titles and release year.

1. Career characterization

Now that we have compiled all needed data, we constructed a new actors-oriented dataframe. This dataframe contains the general information about actors, including details such as the list of movies they have been involved in and whether they have been nominated for an Oscar. Our initial analytical focus will involve a comparative examination of actors' careers, considering various basic characteristics, such as the age at which their careers began, the duration of their careers, and the progression of movie ratings for films in which they participated, among other features.

Drawing inspiration from the research paper that can be found [here](https://www.nature.com/articles/s41467-019-10213-0), our approach will involve the construction of the typical activity pattern of actors. This pattern can be seen as a sequential representation of active years interspersed with latent years without any professional activity. Finally, we aim to employ clustering techniques to categorize actors based on distinct career types.

2. Genres exploration

To explore how actors transition across various genres, our initial step involves unifying genre information from both the [CMU](http://www.cs.cmu.edu/~ark/personas/) and [IMDb](https://www.imdb.com/interfaces/) datasets. Initially, we combine genres and then standardize them. The combined dataset yields over 300 unique genres, making it impractical for analysis. To tackle this issue, we conduct a frequency analysis, identifying the most common words associated with genres. This process results in a refined set of 26 main genres.

Next, we examine movies genres from an actor-centric perspective. By examining the number of movies each actor participated in within each genre, we obtained a distribution of movies for each actor across diverse genres. With this information, we inferred correlations between the proportions of movies associated with pairs of genres. Employing the Pearson correlation coefficient and its associated p-value facilitated this correlation analysis. The Pearson correlation coefficient and its associated p-value was used for that part. 

Moving forward to Milestone P3, our objective is to delve into how actors evolve across different genres. To accomplish this, we plan to construct a Markov Chain, with each state representing a distinct genre and the edges indicating the probabilities of transitioning from one genre to another. Additionally, we aim to integrate genres into our network analysis to observe potential clustering patterns among actors.

3. Network Analysis

We used network analysis to understand and visualize patterns in the film industry. Actors are nodes, and edges represent collaboration through shared appearances in the same movies. Focusing on Oscar-winning actors, our data contains node attributes (e.g., age, gender, ethnicity). 

We examined the graph structure and node importance indices (connected components, diameter, shortest path, transitivity, degree distribution, betweenness centrality, and community detection). The Oscar-winning network is strongly connected; some actors act as hubs, and others bridge between communities.

Future considerations will include how the network changed over time, and if certain actors are less central now than in the past. We will also be analyzing how the global network looks and if we can find communities corresponding to Hollywood, Bollywood, or the French cinema industry ...


4. Ethnicities and Oscars

We explored the influence of actor ethnicity on their careers. Converting Freebase IDs to meaningful strings using a full archive, we conducted basic analyses. Challenges include potential missing values and non-mutually exclusive ethnicities, like 'Jewish people' and 'White people' both being present.

Oscars can be proof of the success of an actor and can have a great impact on their future career; we decided to study them. First, we want to analyze what are the factors that might lead an actor towards an Oscar nomination. In order to do so, we will perform correlation analyses to determine the relationships between potential factors and Oscar nominations. Secondly, we would like to investigate whether actors with previous Oscar nominations or wins are more likely to receive future nominations. This will be done using statistical models like logistic regression to model the likelihood of future nominations based on past nominations or wins.

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
├── 07.12.22 - Construct actors activity pattern
│  
├── 09.12.22 - Construct complete actor network 
│  
├── 10.12.22 - Cluster and analyze actors activity pattern
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




