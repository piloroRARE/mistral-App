import os

from mistralai import Mistral


def main() -> None:
    api_key = os.environ["MISTRAL_API_KEY"]
    client = Mistral(api_key=api_key)

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {"role": "user", "content": "Dis bonjour en une phrase."}
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
