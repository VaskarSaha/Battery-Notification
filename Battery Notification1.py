from plyer import notification
import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if __name__ == "__main__":
    if plugged:
        if percent <= 80:
            message = "For better battery life, charge up to 80%"
        elif percent == 100:
            message = "Please unplug the charger. Battery is charged"
        else:
            message = "Remove the charger please. For better battery life charge up to 80%"
        notification.notify(title="Plugged In", message=message, timeout=2)
    else:
        if percent <= 20:
            message = "Your battery is running low. You might want to plug in your PC"
        elif percent == 100:
            message = "Fully charged"
        else:
            message = f"Battery is {percent}"
        notification.notify(title="Battery Reminder",
                            message=message, timeout=2)
