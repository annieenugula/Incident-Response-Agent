import json
from memory import remember_incident, find_similar_incident


def load_incidents():
    with open("data/incidents.json", "r") as file:
        return json.load(file)


def build_memory():
    incidents = load_incidents()

    for incident in incidents:
        text = (
            f"Incident: {incident['title']}. "
            f"Root cause: {incident['root_cause']}. "
            f"Resolution: {incident['resolution']}. "
            f"Runbook: {incident['runbook']}. "
            f"Lesson: {incident['lesson']}."
        )
        remember_incident(text)

    print("Past incidents stored in Hindsight.")


def investigate(query):
    print("\n🚨 New Incident:", query)

    results = find_similar_incident(query)

    if results:
        best = results[0].text

        print("\n🧠 Hindsight found a similar incident:")
        print(best)

        if "Runbook:" in best:
            runbook = best.split("Runbook:")[1].split(".")[0]
            print("\n📋 Recommended Runbook:", runbook)

        if "Lesson:" in best:
            lesson = best.split("Lesson:")[1].split(".")[0]
            print("\n💡 Lesson:", lesson)

    else:
        print("\n❌ No similar incident found.")


if __name__ == "__main__":
    build_memory()
    investigate(
      "The notification service is failing because messages are stuck in the queue."
    )