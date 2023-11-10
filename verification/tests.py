"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["checkIO"],
            "answer": "CheckIO"
        },
        {
            "input": ["zcheckzz"],
            "answer": "zCheckIO"
        },
        {
            "input": ["SoManyChoicesHere"],
            "answer": "SoManyCheckIOHere"
        }
    ],
    "Extra": [
        {
            "input": ["CheckIO"],
            "answer": "CheckIO"
        },
        {
            "input": ["CcchECKioo"],
            "answer": "CheckIOioo"
        },
        {
            "input": ["zzzzzzzIOzz"],
            "answer": "zzCheckIOzz"
        },
        {
            "input": ["canSomeoneFindIOHere"],
            "answer": "canSomeonCheckIOHere"
        },
        {
            "input": ["checkIoischeckIO"],
            "answer": "checkIoisCheckIO"
        },
        {
            "input": ["zzzzzzzzcheckI"],
            "answer": "zzzzzCheckIOkI"
        },
        {
            "input": ["CheckiozCheckIzz"],
            "answer": "CheckiozCheckIOz"
        },
        {
            "input": ["zChiOCheckI"],
            "answer": "zCheckIOckI"
        },
        {
            "input": ["zzzCheckzzzzCheckiOzzzzCheckiOzzzz"],
            "answer": "zzzCheckzzzzCheckIOzzzzCheckiOzzzz"
        },
        {
            "input": ["zzzCheckIozzCheckiozzzzCheckIozzzz"],
            "answer": "zzzCheckIOzzCheckiozzzzCheckIozzzz"
        },
        {
            "input": ["zzasdfaChedasdfadsfsCheckdsafdasheckIOsadfxvbxozzzz"],
            "answer": "zzasdfaChedasdfadsfsCheckdsafdaCheckIOsadfxvbxozzzz"
        }
    ]
}
