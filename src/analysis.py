import matplotlib.pyplot as plt

def traffic_by_day(df):
    data = df.groupby('day')['Traffic Volume'].mean()

    plt.figure()
    data.plot(kind='bar')
    plt.title("Average Traffic by Day")
    plt.xlabel("Day")
    plt.ylabel("Traffic Volume")
    plt.savefig("outputs/plots/traffic_by_day.png")
    plt.close()


def traffic_vs_weather(df):
    data = df.groupby('Weather Conditions')['Traffic Volume'].mean()

    plt.figure()
    data.plot(kind='bar')
    plt.title("Traffic vs Weather")
    plt.xlabel("Weather")
    plt.ylabel("Traffic Volume")
    plt.savefig("outputs/plots/traffic_weather.png")
    plt.close()


def congestion_analysis(df):
    data = df.groupby('Congestion Level')['Traffic Volume'].mean()

    plt.figure()
    data.plot(kind='bar')
    plt.title("Traffic vs Congestion Level")
    plt.xlabel("Congestion Level")
    plt.ylabel("Traffic Volume")
    plt.savefig("outputs/plots/congestion.png")
    plt.close()