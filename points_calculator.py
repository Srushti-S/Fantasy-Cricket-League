import sqlite3

conn = sqlite3.connect('fantasy.db')
cur = conn.cursor()
cur.execute("SELECT * FROM match;")
row = cur.fetchall()

def calculate_points(row):
    total_pts = 0.0
    score = row[2]
    try:
        strike_rate = float(row[2]) / float(row[3])  # strike rate =runs/balls faced
    except:
        strike_rate = 0
    fours, sixes = float(row[4]), float(row[5])

    points = int((score - 4 * fours - 6 * sixes) / 2) # 1 point for each 2 runs scored
    wk_pts = 10 * float(row[9])
    try:
        eco_rate = float(row[8]) / (float(row[6]) / 6) # economy rate = runs/over
    except:
        eco_rate = 0
    fielding_pt = float(row[10]) + float(row[11]) + float(row[12])

    # 2 point for hitting a boundary ,4 points for over boundary, 10 points each for catch and wicket
    total_pts += (2*fours + 6*sixes + points + 10* fielding_pt + wk_pts)

    if score > 100:
        total_pts += 10  # 10 points for century
    elif score >= 50:
        total_pts += 5  # 5 points for half century

    if strike_rate > 1:  # for strike rate>100
        total_pts += 4
    elif strike_rate >= 0.8:
        total_pts += 2  # 2 points for strike rate >= 80

    if wk_pts >= 5:
        total_pts += 10  # Additional 10 points for 5 wickets
    elif wk_pts > 3:
        total_pts += 5  # Additional 5 points for 3 wickets

    if eco_rate >= 3.5 and eco_rate <= 4.5:
        total_pts += 4  # 4 points for eco rate between 3.5 and 4.5
    elif eco_rate >= 2 and eco_rate < 3.5:
        total_pts += 7  # 7 points for economy rate between 2 and 3.5
    elif eco_rate < 2:
        total_pts += 10  # 10 points for economy rate less than 2

    return total_pts

#player_points = {} #for printing calculated points
for i in row:
   # player_points[i[0]] = calculate_points(i) 
    try:
        cur.execute(" UPDATE match SET points ='"+ str(calculate_points(i)) +"' WHERE player= '"+i[0]+"'  ;")
        conn.commit()  
    except:        
        conn.rollback()
        
#print(player_points)
