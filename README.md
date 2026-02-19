# DSC 2130 – Sports Analytics  
## Final Project – Part 1: Data Construction  

### Group Name: We Bare Bears 🐻

**Team Members:**  
- Jayden Cruz  
- Peter Hoand  
- Mayur Patel  

---

## Project Overview  

This project represents Part 1 of our DSC 2130 Sports Analytics Final Project.  
The focus of this phase is **Data Construction**, which involves organizing, cleaning, and enriching a professional-level badminton dataset for analytical use.

The dataset tracks cumulative BWF World Tour performance from 2018–2023 and includes 185 professional players.

---

## Dataset Information  

- **Dataset Name:** `badminton_wrld_tour.csv`  
- **Sport:** Badminton (BWF World Tour)  
- **Season Coverage:** 2018–2023  
- **Observations:** 185 players  
- **Variables:** 12 total (9 original + 3 derived)  
- **Source:** SCORE Sports Data Repository (Smith, 2024)  

The original dataset included aggregate performance statistics such as matches, wins, losses, and total points scored and conceded.

---

## Original Variables  

1. `player_name` – Player’s full name  
2. `discipline` – Singles or Doubles  
3. `matches_played` – Total matches played (2018–2023)  
4. `wins` – Total matches won  
5. `losses` – Total matches lost  
6. `pts_for` – Total rally points scored  
7. `pts_agst` – Total rally points conceded  
8. `win_pct` – Win percentage (wins / matches_played)  
9. `shot_pct` – Point share percentage (pts_for / total points played)  

---

## Derived Variables  

To improve analytical depth and allow fair comparisons across players with different match volumes, three additional variables were created:

1. **`pt_differential`**  
   - Formula: `pts_for – pts_agst`  
   - Measures overall net point margin  

2. **`pt_differential_per_match`**  
   - Formula: `pt_differential / matches_played`  
   - Standardizes scoring margin by match volume  

3. **`experience_tier`**  
   - Ordinal classification based on matches played:  
     - Low (1–5)  
     - Moderate (6–20)  
     - High (21–50)  
     - Elite (51+)  
   - Allows grouping players by competitive exposure  

---

## Data Cleaning & Transformation  

- Renamed all columns to consistent `snake_case` formatting  
- Rounded `win_pct` and `shot_pct` to 4 decimal places  
- Rounded `pt_differential_per_match` to 2 decimal places  
- Verified no missing values were present  
- Verified no duplicate player rows  
- Dropped original CSV index column  
- Final dataset indexed 0–184  

No missing or duplicate values were found in either the original or final dataset.

---

## Potential Analysis  

One potential analysis using the dataset is a linear regression model examining whether total points scored (`pts_for`) predicts wins.  
This could also be extended by testing differences between Singles and Doubles players using interaction terms or separate models.

---

## Data Sources  

- Smith, A. (2024). *2018–2023 Badminton World Tour points head-to-head*. SCORE Sports Data Repository.  
- Badminton Statistics (2023)  
- Badminton World Federation (2023)  

