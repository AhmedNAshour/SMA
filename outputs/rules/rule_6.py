def findDecision(obj): #obj[0]: Fever, obj[1]: Tiredness, obj[2]: Dry-Cough, obj[3]: Difficulty-in-Breathing, obj[4]: Sore-Throat, obj[5]: Pains, obj[6]: Nasal-Congestion, obj[7]: Runny-Nose, obj[8]: Diarrhea, obj[9]: Smell and taste loss
   # {"feature": "Nasal-Congestion", "instances": 26739, "metric_value": 0.9567, "depth": 1}
   if obj[6]<=0.0:
      # {"feature": "Smell and taste loss", "instances": 17762, "metric_value": 0.9862, "depth": 2}
      if obj[9]>0:
         # {"feature": "Pains", "instances": 12942, "metric_value": 0.976, "depth": 3}
         if obj[5]<=0:
            # {"feature": "Fever", "instances": 7666, "metric_value": 0.7309, "depth": 4}
            if obj[0]<=0:
               # {"feature": "Dry-Cough", "instances": 4368, "metric_value": 0.2642, "depth": 5}
               if obj[2]>0:
                  return 'yes'
               elif obj[2]<=0:
                  # {"feature": "Runny-Nose", "instances": 2068, "metric_value": 0.4522, "depth": 6}
                  if obj[7]<=0:
                     # {"feature": "Sore-Throat", "instances": 1119, "metric_value": 0.6694, "depth": 7}
                     if obj[4]<=0:
                        # {"feature": "Diarrhea", "instances": 745, "metric_value": 0.8314, "depth": 8}
                        if obj[8]<=0:
                           # {"feature": "Tiredness", "instances": 412, "metric_value": 0.91, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 311, "metric_value": 0.9862, "depth": 10}
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
                           # {"feature": "Tiredness", "instances": 333, "metric_value": 0.6934, "depth": 9}
                           if obj[1]<=0:
                              return 'yes'
                           elif obj[1]>0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 161, "metric_value": 0.9616, "depth": 10}
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
               # {"feature": "Sore-Throat", "instances": 3298, "metric_value": 0.9795, "depth": 5}
               if obj[4]<=0:
                  # {"feature": "Runny-Nose", "instances": 1659, "metric_value": 0.3899, "depth": 6}
                  if obj[7]<=0:
                     # {"feature": "Diarrhea", "instances": 871, "metric_value": 0.5993, "depth": 7}
                     if obj[8]>0:
                        # {"feature": "Dry-Cough", "instances": 482, "metric_value": 0.832, "depth": 8}
                        if obj[2]<=0:
                           # {"feature": "Tiredness", "instances": 304, "metric_value": 0.9804, "depth": 9}
                           if obj[1]>0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 222, "metric_value": 0.985, "depth": 10}
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
                  # {"feature": "Difficulty-in-Breathing", "instances": 1639, "metric_value": 0.7957, "depth": 6}
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
            # {"feature": "Runny-Nose", "instances": 5276, "metric_value": 0.8736, "depth": 4}
            if obj[7]<=0:
               # {"feature": "Dry-Cough", "instances": 3347, "metric_value": 0.993, "depth": 5}
               if obj[2]<=0:
                  # {"feature": "Difficulty-in-Breathing", "instances": 2499, "metric_value": 0.8335, "depth": 6}
                  if obj[3]<=0:
                     # {"feature": "Fever", "instances": 2296, "metric_value": 0.7209, "depth": 7}
                     if obj[0]<=0:
                        # {"feature": "Sore-Throat", "instances": 2116, "metric_value": 0.5612, "depth": 8}
                        if obj[4]<=0:
                           # {"feature": "Tiredness", "instances": 2027, "metric_value": 0.4472, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Diarrhea", "instances": 1609, "metric_value": 0.3161, "depth": 10}
                              if obj[8]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[1]>0:
                              # {"feature": "Diarrhea", "instances": 418, "metric_value": 0.7816, "depth": 10}
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
               # {"feature": "Sore-Throat", "instances": 1929, "metric_value": 0.1484, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Tiredness", "instances": 1900, "metric_value": 0.0552, "depth": 6}
                  if obj[1]>0:
                     # {"feature": "Difficulty-in-Breathing", "instances": 1893, "metric_value": 0.0264, "depth": 7}
                     if obj[3]<=0:
                        return 'no'
                     elif obj[3]>0:
                        # {"feature": "Fever", "instances": 253, "metric_value": 0.1401, "depth": 8}
                        if obj[0]>0:
                           # {"feature": "Diarrhea", "instances": 251, "metric_value": 0.0935, "depth": 9}
                           if obj[8]>0:
                              # {"feature": "Dry-Cough", "instances": 250, "metric_value": 0.0672, "depth": 10}
                              if obj[2]<=1:
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
                  elif obj[1]<=0:
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[4]<=0:
                  return 'yes'
               else:
                  return 'yes'
            else:
               return 'no'
         else:
            return 'no'
      elif obj[9]<=0:
         # {"feature": "Sore-Throat", "instances": 4820, "metric_value": 0.0118, "depth": 3}
         if obj[4]>0:
            return 'no'
         elif obj[4]<=0:
            # {"feature": "Dry-Cough", "instances": 1992, "metric_value": 0.0253, "depth": 4}
            if obj[2]<=0:
               # {"feature": "Difficulty-in-Breathing", "instances": 1989, "metric_value": 0.0115, "depth": 5}
               if obj[3]<=0:
                  # {"feature": "Fever", "instances": 1922, "metric_value": 0.0064, "depth": 6}
                  if obj[0]<=0:
                     return 'no'
                  elif obj[0]>0:
                     # {"feature": "Tiredness", "instances": 135, "metric_value": 0.0631, "depth": 7}
                     if obj[1]<=1:
                        # {"feature": "Pains", "instances": 135, "metric_value": 0.0631, "depth": 8}
                        if obj[5]<=0:
                           # {"feature": "Runny-Nose", "instances": 135, "metric_value": 0.0631, "depth": 9}
                           if obj[7]<=0:
                              # {"feature": "Diarrhea", "instances": 135, "metric_value": 0.0631, "depth": 10}
                              if obj[8]<=1:
                                 return 'no'
                              else:
                                 return 'no'
                           else:
                              return 'no'
                        else:
                           return 'no'
                     else:
                        return 'no'
                  else:
                     return 'no'
               elif obj[3]>0:
                  # {"feature": "Pains", "instances": 67, "metric_value": 0.1119, "depth": 6}
                  if obj[5]<=0:
                     return 'no'
                  elif obj[5]>0:
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'no'
            elif obj[2]>0:
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
