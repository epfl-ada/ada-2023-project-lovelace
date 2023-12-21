# Behind the Scenes of Stardom: Decoding the Patterns in Actors' Careers  <img src="Data/Images/LinkedIn_logo_initials.png" alt="LinkedIn Logo" width="25" height="25">

## Abstract
How do you envision your career? We, as scientists, will probably spend a substantial portion of our career in the same company in a specific field, like pharma, robotics or data science for the most talented of us. For actors, the journey is more complex, involving potential shifts between diverse movie genres and marked by the inevitable highs and lows inherent to the profession. In our project, we aim at analyzing the trajectory of acting careers. 

Usually, when you seek information about someone's career, you turn to LinkedIn. Would you do the same to stalk your childhood actor crush? Well, good news, we are here to do it for you. From the number of connections (actors they have collaborated with), to the potential genre specialization in movies, and not forgetting the prospect of winning an Oscar, let’s delve into the intricacies of our actors’ careers. 

## Research Questions

1. What characterizes the career trajectories of actors?
2. How do actors navigate and evolve across various genres throughout their careers?
3. Are there observable patterns in the network connecting actors?
4. When do actors potentially receive an Oscar ?

## Additional Datasets 

- [**IMDb Datasets**](https://www.imdb.com/interfaces/) - We incorporated one IMDb datasets, namely `title.basics`. This was useful for the genre analysis as there exists only 29 unique genres compared to 362 genres present in CMU. Upon merging with our [**CMU Movie Summary Corpus**](http://www.cs.cmu.edu/~ark/personas/), we achieved a matching rate of 62%.

- [**Oscars**](https://www.kaggle.com/datasets/unanimad/the-oscar-award) - The Oscars dataset, sourced from Kaggle and scraped from the Official Academy Awards site, spans nominations from $1927$ to $2022$ across various categories. For our analysis, we retain only categories related to actors.

- [**Freebase dataset**](https://developers.google.com/freebase) - We utilized the archive of the Freebase database to convert the Freebase Ethnicity IDs to text strings.

## Methods

0. Merging the datasets

The first step of our analysis is to merge the different datasets we are using. As they are not sourced from the same database, they don't have a common unique identifier. Therefore, we had no choice but to merge on names of either movies or actors. This poses an issue, as a title can be written in different formats, and the matching might not be exact. For example, the title 'Harry Potter and the Deathly Hallows Part I' can also be written as 'Harry Potter and the Deathly Hallows Part 1'. In this case, the standard matching will not work. To resolve this problem, we first standardize the titles by removing special characters and setting all the characters to lowercase. We then use Fuzzy Matching with the `rapidfuzz` library to match movie titles that are sufficiently close to each other using the WRatio similarity metric. We can then perform the merge on the matched titles and release year.

1. Career Characterization

Now that we have compiled all needed data, we constructed a new actors-oriented dataframe. This dataframe contains the general information about actors, including details such as the list of movies they have been involved in and whether they have been nominated for an Oscar. 

Drawing inspiration from the research paper that can be found [here](https://www.nature.com/articles/s41467-019-10213-0), our approach involves the construction of the typical activity pattern of actors, denoting the number of movies done by an actor for each year of his career. Following this, we utilized clustering techniques, including the Silhouette score to determine the optimal number of clusters, and k-means, to categorize actors into distinct career types.

Our analysis then delves into specific aspects of acting trajectories, including the age at which careers started, the duration of their careers, and the correlation between the number of active years and the overall length of their career. Furthermore, we explore potential gender bias in all the factors under consideration.

2. Genres Exploration

In this section, we examine movies genres from an actor-centric perspective. By examining the number of movies each actor participated in within each genre, we obtained a distribution of movies for each actor across diverse genres. With this information, we inferred correlations between the proportions of movies associated with pairs of genres. Employing the Pearson correlation coefficient and its associated p-value facilitated this correlation analysis. The Pearson correlation coefficient and its associated p-value was used for that part. 

Following this, we cluster actors based on their genre proportions using k-means, as described in part 1. This clustering allows us to compare different characteristics of actors within each cluster. Subsequently, we employ ANOVA to confirm differences between these clusters.

Then to quantify how extensively actors explore different genres in our dataset, we utilize the Normalized Hill's Herfindahl Index (NHHI).

Finally, our objective is to delve into how actors evolve across different genres. To achieve this, we construct a Markov Chain wherein each state represents a distinct genre, and the edges indicate the probabilities of transitioning from one genre to another. This approach helps us define a steady-state genre distribution in different time periods and understand the genres in which actors spend the majority of their careers on average.

3. Network Analysis

We used network analysis to understand and visualize patterns in the film industry. Actors are nodes, and edges represent collaboration through shared appearances in the same movies. Focusing on Oscar-winning actors, our network contains node attributes related to age, gender, ethnicity, etc. 

We examined the graph structure and node importance indices (connected components, diameter, shortest path, transitivity, degree distribution, betweenness centrality, and community detection). The Oscar-winning network is strongly connected; some actors act as hubs, and others bridge between communities.

Future considerations will include how the network changed over time, and if certain actors are less central now than in the past. We will also be analyzing how the global network looks and if we can find communities corresponding to Hollywood, Bollywood, or the French cinema industry ...


4. Oscars

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
├── 07.12.22 - Construct genres Markov chains, actors profile sequence, and actors network
│  
├── 07.12.22 - Start analysis
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

- Jennifer Abou-Najm : Career characterization (Data Story and Analysis)
- Mariem Boughzala :  Network analysis (Data Story and Analysis)
- Valérie Costa : Dataset merging, genres exploration (Data Story and Analysis)
- Michael Ha : Dataset merging, Oscars analysis (Data Story and Analysis)
- Adrien Vannson : Ethnicities dataset extraction, website creation




