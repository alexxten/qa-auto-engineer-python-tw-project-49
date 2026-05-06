import random

import prompt

from brain_games.cli import welcome_user


def is_user_answer_correct(*, user_answer: str, num: int) -> tuple[bool, str]:
    expected_answer = "yes" if num % 2 == 0 else "no"
    return user_answer == expected_answer, expected_answer


def evenness_check():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    questions_count = 3
    while questions_count > 0:
        num = random.randint(1, 1000)
        print(f"Question: {num}")
        user_answer = prompt.string("Your answer: ")
        user_answer_correct, expected_answer = is_user_answer_correct(
            user_answer=user_answer,
            num=num,
        )
        if user_answer_correct:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{expected_answer}'.\n"
                f"Let's try again, {user_name}!"
            )
            return
        questions_count -= 1
    print(f"Congratulations, {user_name}!")


def main():
    evenness_check()


if __name__ == '__main__':
    main()