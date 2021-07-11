def findDecision(obj): #obj[0]: Fever, obj[1]: Tiredness, obj[2]: Dry-Cough, obj[3]: Difficulty-in-Breathing, obj[4]: Sore-Throat, obj[5]: Pains, obj[6]: Nasal-Congestion, obj[7]: Runny-Nose, obj[8]: Diarrhea, obj[9]: Smell and taste loss
   # {"feature": "Smell and taste loss", "instances": 26739, "metric_value": 0.9479, "depth": 1}
   if obj[9]>0:
      # {"feature": "Nasal-Congestion", "instances": 22100, "metric_value": 0.7846, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Pains", "instances": 12983, "metric_value": 0.9698, "depth": 3}
         if obj[5]<=0:
            # {"feature": "Fever", "instances": 7760, "metric_value": 0.7139, "depth": 4}
            if obj[0]<=0:
               # {"feature": "Dry-Cough", "instances": 4480, "metric_value": 0.2661, "depth": 5}
               if obj[2]>0:
                  return 'yes'
               elif obj[2]<=0:
                  # {"feature": "Runny-Nose", "instances": 2115, "metric_value": 0.4561, "depth": 6}
                  if obj[7]<=0:
                     # {"feature": "Sore-Throat", "instances": 1152, "metric_value": 0.6717, "depth": 7}
                     if obj[4]<=0:
                        # {"feature": "Diarrhea", "instances": 775, "metric_value": 0.8297, "depth": 8}
                        if obj[8]<=0:
                           # {"feature": "Tiredness", "instances": 431, "metric_value": 0.8942, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 334, "metric_value": 0.9716, "depth": 10}
                              if obj[3]>0:
                                 return 'yes'
                              elif obj[3]<=0:
                                 return 'yes'
                              else:
                                 return 'yes'
                           elif obj[1]>0:
                              return 'yes'
                           else:
                              return 'yes'
                        elif obj[8]>0:
                           # {"feature": "Tiredness", "instances": 344, "metric_value": 0.7231, "depth": 9}
                           if obj[1]<=0:
                              return 'yes'
                           elif obj[1]>0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 154, "metric_value": 0.9922, "depth": 10}
                              if obj[3]<=0:
                                 return 'yes'
                              else:
                                 return 'yes'
                           else:
                              return 'yes'
                        else:
                           return 'yes'
                     elif obj[4]>0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[7]>0:
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'yes'
            elif obj[0]>0:
               # {"feature": "Sore-Throat", "instances": 3280, "metric_value": 0.972, "depth": 5}
               if obj[4]<=0:
                  # {"feature": "Runny-Nose", "instances": 1690, "metric_value": 0.363, "depth": 6}
                  if obj[7]<=0:
                     # {"feature": "Diarrhea", "instances": 870, "metric_value": 0.5696, "depth": 7}
                     if obj[8]>0:
                        # {"feature": "Dry-Cough", "instances": 483, "metric_value": 0.7987, "depth": 8}
                        if obj[2]<=0:
                           # {"feature": "Tiredness", "instances": 301, "metric_value": 0.964, "depth": 9}
                           if obj[1]>0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 210, "metric_value": 0.9906, "depth": 10}
                              if obj[3]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[1]<=0:
                              return 'yes'
                           else:
                              return 'yes'
                        elif obj[2]>0:
                           return 'yes'
                        else:
                           return 'yes'
                     elif obj[8]<=0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[7]>0:
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[4]>0:
                  # {"feature": "Difficulty-in-Breathing", "instances": 1590, "metric_value": 0.8027, "depth": 6}
                  if obj[3]<=0:
                     return 'no'
                  elif obj[3]>0:
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'no'
            else:
               return 'yes'
         elif obj[5]>0:
            # {"feature": "Runny-Nose", "instances": 5223, "metric_value": 0.8836, "depth": 4}
            if obj[7]<=0:
               # {"feature": "Dry-Cough", "instances": 3335, "metric_value": 0.995, "depth": 5}
               if obj[2]<=0:
                  # {"feature": "Difficulty-in-Breathing", "instances": 2472, "metric_value": 0.8406, "depth": 6}
                  if obj[3]<=0:
                     # {"feature": "Fever", "instances": 2257, "metric_value": 0.7216, "depth": 7}
                     if obj[0]<=0:
                        # {"feature": "Sore-Throat", "instances": 2077, "metric_value": 0.5587, "depth": 8}
                        if obj[4]<=0:
                           # {"feature": "Tiredness", "instances": 1989, "metric_value": 0.4431, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Diarrhea", "instances": 1597, "metric_value": 0.3025, "depth": 10}
                              if obj[8]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[1]>0:
                              # {"feature": "Diarrhea", "instances": 392, "metric_value": 0.8072, "depth": 10}
                              if obj[8]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           else:
                              return 'no'
                        elif obj[4]>0:
                           return 'yes'
                        else:
                           return 'yes'
                     elif obj[0]>0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[3]>0:
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[2]>0:
                  return 'yes'
               else:
                  return 'yes'
            elif obj[7]>0:
               # {"feature": "Sore-Throat", "instances": 1888, "metric_value": 0.1709, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Difficulty-in-Breathing", "instances": 1852, "metric_value": 0.0564, "depth": 6}
                  if obj[3]<=0:
                     # {"feature": "Tiredness", "instances": 1621, "metric_value": 0.0075, "depth": 7}
                     if obj[1]>0:
                        return 'no'
                     elif obj[1]<=0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[3]>0:
                     # {"feature": "Fever", "instances": 231, "metric_value": 0.2762, "depth": 7}
                     if obj[0]>0:
                        # {"feature": "Diarrhea", "instances": 224, "metric_value": 0.1292, "depth": 8}
                        if obj[8]>0:
                           # {"feature": "Tiredness", "instances": 222, "metric_value": 0.0741, "depth": 9}
                           if obj[1]<=1:
                              # {"feature": "Dry-Cough", "instances": 222, "metric_value": 0.0741, "depth": 10}
                              if obj[2]<=1:
                                 return 'no'
                              else:
                                 return 'no'
                           else:
                              return 'no'
                        elif obj[8]<=0:
                           return 'yes'
                        else:
                           return 'yes'
                     elif obj[0]<=0:
                        return 'yes'
                     else:
                        return 'yes'
                  else:
                     return 'no'
               elif obj[4]<=0:
                  return 'yes'
               else:
                  return 'yes'
            else:
               return 'no'
         else:
            return 'no'
      elif obj[6]>0.0:
         return 'yes'
      else:
         return 'yes'
   elif obj[9]<=0:
      # {"feature": "Nasal-Congestion", "instances": 4639, "metric_value": 0.0163, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Difficulty-in-Breathing", "instances": 4636, "metric_value": 0.01, "depth": 3}
         if obj[3]<=0:
            # {"feature": "Sore-Throat", "instances": 4351, "metric_value": 0.0031, "depth": 4}
            if obj[4]>0:
               return 'no'
            elif obj[4]<=0:
               # {"feature": "Dry-Cough", "instances": 1842, "metric_value": 0.0067, "depth": 5}
               if obj[2]<=0:
                  return 'no'
               elif obj[2]>0:
                  return 'yes'
               else:
                  return 'yes'
            else:
               return 'no'
         elif obj[3]>0:
            # {"feature": "Fever", "instances": 285, "metric_value": 0.0843, "depth": 4}
            if obj[0]>0:
               return 'no'
            elif obj[0]<=0:
               # {"feature": "Sore-Throat", "instances": 70, "metric_value": 0.2552, "depth": 5}
               if obj[4]<=0:
                  # {"feature": "Tiredness", "instances": 68, "metric_value": 0.1106, "depth": 6}
                  if obj[1]<=0:
                     return 'no'
                  elif obj[1]>0:
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[4]>0:
                  return 'yes'
               else:
                  return 'yes'
            else:
               return 'no'
         else:
            return 'no'
      elif obj[6]>0.0:
         return 'yes'
      else:
         return 'yes'
   else:
      return 'no'
