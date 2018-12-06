def divide(numerator,denominator):
    try:
        result = numerator/denominator
        print(result)
    except ValueError:
        raise Exception('Only number accepted')
    except ZeroDivisionError:
        raise Exception('zero cant be the denominator')
    except:
        raise Exception('Either one of the argument is invalid')
    finally:
        print('we are done!')


try:
    divide(10,0)
except Exception as error:
    print(error)


try:
    divide(10,"a")
except Exception as error:
    print(error)