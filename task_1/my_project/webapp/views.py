from django.shortcuts import render


def calculator_view(request):
    calc_result = {}
    if request.method == 'GET':
        return render(request, 'calculator.html')
    elif request.method == 'POST':
        nums = request.POST
        first_num_tup = nums.get('first_num'),
        second_num_tup = nums.get('second_num'),
        operation = nums.get('operation')
        first_num = first_num_tup[0]
        second_num = second_num_tup[0]

        if operation == 'add':
            if '.' in first_num or '.' in second_num:
                result = float(first_num) + float(second_num)
                spl_result = str(result).split('.')
                if spl_result[1] == '0':
                    result = spl_result[0]
            else:
                result = int(first_num) + int(second_num)

            calc_result = {'calc_result': f'Result: {first_num} + {second_num} = {result}'}
        elif operation == 'subtract':
            if '.' in first_num or '.' in second_num:
                result = float(first_num) - float(second_num)
                spl_result = str(result).split('.')
                if spl_result[1] == '0':
                    result = spl_result[0]
            else:
                result = int(first_num) - int(second_num)

            calc_result = {'calc_result': f'Result: {first_num} - {second_num} = {result}'}
        elif operation == 'multiply':
            if '.' in first_num or '.' in second_num:
                result = float(first_num) * float(second_num)
                spl_result = str(result).split('.')
                if spl_result[1] == '0':
                    result = spl_result[0]
            else:
                result = int(first_num) * int(second_num)

            calc_result = {'calc_result': f'Result: {first_num} * {second_num} = {result}'}

        elif operation == 'divide':
            if second_num == '0':
                result = "Can't divide by zero"
            elif '.' in first_num or '.' in second_num:
                result = float(first_num) / float(second_num)
                spl_result = str(result).split('.')
                if spl_result[1] == '0':
                    result = spl_result[0]
            else:
                result = int(first_num) / int(second_num)
                if '.' in str(result):
                    spl_result = str(result).split('.')
                    if spl_result[1] == '0':
                        result = spl_result[0]

            calc_result = {'calc_result': f'Result: {first_num} / {second_num} = {result}'}

    return render(request, 'calculator.html', context=calc_result)
