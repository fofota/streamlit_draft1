from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Read the CSV file into a pandas DataFrame
full_df = pd.read_csv('parsed_data.csv')

@app.route('/')
def index():
    # Select specific columns
    selected_columns = ['Inf', 'Name', 'Age', 'Wage', 'Transfer Value', 'Nat', 'Position', 'Personality', 'Av Rat', 'Mins', 'Gls', 'Ast', 'NP-xG/90', 'xA/90']
    df = full_df[selected_columns]

    return render_template('index.html', table=df)

@app.route('/player/<name>')
def player_page(name):
    # Filter the DataFrame based on the selected name
    player_df = full_df[full_df['Name'] == name]

    # Check if the player was found
    if player_df.empty:
        return render_template('player_not_found.html', name=name)

    # Convert the player DataFrame to HTML
    player_html = player_df.to_html(classes='table table-dark', index=False)

    return render_template('player.html', name=name, player_df=player_df, player_table=player_html)


if __name__ == '__main__':
    app.run(debug=True)
