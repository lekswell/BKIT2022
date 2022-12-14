Feature: Sorting

    Scenario: Seq1
        Given the list is [3, -4, 5, 2, 1]
        When the list is sorted
        Then the new list is [5, -4, 3, 2, 1]
    
     Scenario: Seq2
        Given the list is [3, -4, 8, 5, 0, 1, -1, 17]
        When the list is sorted2
        Then the new list is [17, 8, 5, -4, 3, 1, -1, 0]

    Scenario: Seq3
        Given the list is [0, -100, 100, 67, 67, 99, 15, 16, -15]
        When the list is sorted3
        Then the new list is [-100, 100, 99, 67, 67, 16, 15, -15, 0]