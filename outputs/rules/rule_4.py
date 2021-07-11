def findDecision(obj): #obj[0]: Fever, obj[1]: Tiredness, obj[2]: Dry-Cough, obj[3]: Difficulty-in-Breathing, obj[4]: Sore-Throat, obj[5]: Pains, obj[6]: Nasal-Congestion, obj[7]: Runny-Nose, obj[8]: Diarrhea, obj[9]: Smell and taste loss
   # {"feature": "Smell and taste loss", "instances": 26739, "metric_value": 0.9542, "depth": 1}
   if obj[9]>0:
      # {"feature": "Nasal-Congestion", "instances": 21924, "metric_value": 0.7912, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Pains", "instances": 12928, "metric_value": 0.9728, "depth": 3}
         if obj[5]<=0:
            # {"feature": "Fever", "instances": 7725, "metric_value": 0.7261, "depth": 4}
            if obj[0]<=0:
               # {"feature": "Dry-Cough", "instances": 4391, "metric_value": 0.2702, "depth": 5}
               if obj[2]>0:
                  return 'yes'
               elif obj[2]<=0:
                  # {"feature": "Runny-Nose", "instances": 2101, "metric_value": 0.4582, "depth": 6}
                  if obj[7]<=0:
                     # {"feature": "Sore-Throat", "instances": 1143, "metric_value": 0.6748, "depth": 7}
                     if obj[4]<=0:
                        # {"feature": "Diarrhea", "instances": 752, "metric_value": 0.8414, "depth": 8}
                        if obj[8]<=0:
                           # {"feature": "Tiredness", "instances": 392, "metric_value": 0.9032, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 298, "metric_value": 0.9812, "depth": 10}
                              if obj[3]<=0:
                                 return 'yes'
                              elif obj[3]>0:
                                 return 'yes'
                              else:
                                 return 'yes'
                           elif obj[1]>0:
                              return 'yes'
                           else:
                              return 'yes'
                        elif obj[8]>0:
                           # {"feature": "Tiredness", "instances": 360, "metric_value": 0.754, "depth": 9}
                           if obj[1]<=0:
                              return 'yes'
                           elif obj[1]>0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 176, "metric_value": 0.9907, "depth": 10}
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
               # {"feature": "Sore-Throat", "instances": 3334, "metric_value": 0.9751, "depth": 5}
               if obj[4]<=0:
                  # {"feature": "Dry-Cough", "instances": 1724, "metric_value": 0.3941, "depth": 6}
                  if obj[2]<=0:
                     # {"feature": "Tiredness", "instances": 915, "metric_value": 0.6009, "depth": 7}
                     if obj[1]>0:
                        # {"feature": "Diarrhea", "instances": 510, "metric_value": 0.8309, "depth": 8}
                        if obj[8]>0:
                           # {"feature": "Runny-Nose", "instances": 324, "metric_value": 0.9783, "depth": 9}
                           if obj[7]<=0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 236, "metric_value": 0.9867, "depth": 10}
                              if obj[3]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[7]>0:
                              return 'yes'
                           else:
                              return 'yes'
                        elif obj[8]<=0:
                           return 'yes'
                        else:
                           return 'yes'
                     elif obj[1]<=0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[2]>0:
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[4]>0:
                  # {"feature": "Difficulty-in-Breathing", "instances": 1610, "metric_value": 0.7946, "depth": 6}
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
            # {"feature": "Runny-Nose", "instances": 5203, "metric_value": 0.8792, "depth": 4}
            if obj[7]<=0:
               # {"feature": "Dry-Cough", "instances": 3303, "metric_value": 0.9943, "depth": 5}
               if obj[2]<=0:
                  # {"feature": "Sore-Throat", "instances": 2444, "metric_value": 0.8332, "depth": 6}
                  if obj[4]<=0:
                     # {"feature": "Fever", "instances": 2249, "metric_value": 0.723, "depth": 7}
                     if obj[0]<=0:
                        # {"feature": "Difficulty-in-Breathing", "instances": 2087, "metric_value": 0.5802, "depth": 8}
                        if obj[3]<=0:
                           # {"feature": "Tiredness", "instances": 1988, "metric_value": 0.4548, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Diarrhea", "instances": 1588, "metric_value": 0.3167, "depth": 10}
                              if obj[8]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[1]>0:
                              # {"feature": "Diarrhea", "instances": 400, "metric_value": 0.8073, "depth": 10}
                              if obj[8]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           else:
                              return 'no'
                        elif obj[3]>0:
                           return 'yes'
                        else:
                           return 'yes'
                     elif obj[0]>0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[4]>0:
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[2]>0:
                  return 'yes'
               else:
                  return 'yes'
            elif obj[7]>0:
               # {"feature": "Sore-Throat", "instances": 1900, "metric_value": 0.1673, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Tiredness", "instances": 1862, "metric_value": 0.0441, "depth": 6}
                  if obj[1]>0:
                     # {"feature": "Difficulty-in-Breathing", "instances": 1859, "metric_value": 0.0314, "depth": 7}
                     if obj[3]<=0:
                        return 'no'
                     elif obj[3]>0:
                        # {"feature": "Diarrhea", "instances": 229, "metric_value": 0.175, "depth": 8}
                        if obj[8]>0:
                           # {"feature": "Fever", "instances": 226, "metric_value": 0.1018, "depth": 9}
                           if obj[0]>0:
                              # {"feature": "Dry-Cough", "instances": 225, "metric_value": 0.0733, "depth": 10}
                              if obj[2]<=1:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[0]<=0:
                              return 'yes'
                           else:
                              return 'yes'
                        elif obj[8]<=0:
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
      elif obj[6]>0.0:
         return 'yes'
      else:
         return 'yes'
   elif obj[9]<=0:
      # {"feature": "Nasal-Congestion", "instances": 4815, "metric_value": 0.0196, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Difficulty-in-Breathing", "instances": 4810, "metric_value": 0.0097, "depth": 3}
         if obj[3]<=0:
            # {"feature": "Sore-Throat", "instances": 4519, "metric_value": 0.003, "depth": 4}
            if obj[4]>0:
               return 'no'
            elif obj[4]<=0:
               # {"feature": "Fever", "instances": 1908, "metric_value": 0.0065, "depth": 5}
               if obj[0]<=0:
                  return 'no'
               elif obj[0]>0:
                  # {"feature": "Pains", "instances": 122, "metric_value": 0.0686, "depth": 6}
                  if obj[5]<=0:
                     return 'no'
                  elif obj[5]>0:
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'no'
            else:
               return 'no'
         elif obj[3]>0:
            # {"feature": "Pains", "instances": 291, "metric_value": 0.0828, "depth": 4}
            if obj[5]>0:
               return 'no'
            elif obj[5]<=0:
               # {"feature": "Dry-Cough", "instances": 74, "metric_value": 0.2448, "depth": 5}
               if obj[2]<=0:
                  # {"feature": "Sore-Throat", "instances": 72, "metric_value": 0.1056, "depth": 6}
                  if obj[4]<=0:
                     return 'no'
                  elif obj[4]>0:
                     return 'yes'
                  else:
                     return 'yes'
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
   else:
      return 'no'
