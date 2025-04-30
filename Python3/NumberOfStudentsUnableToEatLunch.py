# This solution is the most verbose
# And actually act out the idea of a student leaving the line and getting back in
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # While we have hungry students
        while students:
            # If the next student likes the sandwich on top of the stack
            if students[0] == sandwiches[0]:
                # Then they are satisfied and will take the sandwich
                students.pop(0)
                sandwiches.pop(0)
            # If they don't like it
            else:
                # And if there is no one else left that likes it
                if sandwiches[0] not in set(students):
                    # Then all our leftover students will go hungry
                    break
                # But if someone will eat it, then this student will get back in line and try again
                students.append(students[0])
                students.pop(0)

        return len(students)
    
# Alternate Solution
# This solution takes advantage of the fact that the order of the students doesn't matter
# and only the order of the sandwiches matters
class Solution2:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Start by assuming all of our students will go hungry
        result = len(students)
        # And find out how many students like which sandwich
        count = Counter(students)

        # For every sandwich
        for s in sandwiches:
            # If there is a student that's willing to eat it
            if count[s] > 0:
                # Then we have one less hungry student, and one less student willing to eat the sandwich
                result -= 1
                count[s] -= 1
            # But if there's not one, then the rest of our students will go hungry
            else:
                break
        
        return result