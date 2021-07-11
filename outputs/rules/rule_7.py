def findDecision(obj): #obj[0]: Fever, obj[1]: Tiredness, obj[2]: Dry-Cough, obj[3]: Difficulty-in-Breathing, obj[4]: Sore-Throat, obj[5]: Pains, obj[6]: Nasal-Congestion, obj[7]: Runny-Nose, obj[8]: Diarrhea, obj[9]: Smell and taste loss
   # {"feature": "Smell and taste loss", "instances": 26739, "metric_value": 0.9499, "depth": 1}
   if obj[9]>0:
      # {"feature": "Nasal-Congestion", "instances": 22011, "metric_value": 0.7845, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Pains", "instances": 12982, "metric_value": 0.9688, "depth": 3}
         if obj[5]<=0:
            # {"feature": "Fever", "instances": 7827, "metric_value": 0.7177, "depth": 4}
            if obj[0]<=0:
               # {"feature": "Dry-Cough", "instances": 4553, "metric_value": 0.2849, "depth": 5}
               if obj[2]>0:
                  return 'yes'
               elif obj[2]<=0:
                  # {"feature": "Runny-Nose", "instances": 2205, "metric_value": 0.4769, "depth": 6}
                  if obj[7]<=0:
                     # {"feature": "Sore-Throat", "instances": 1182, "metric_value": 0.704, "depth": 7}
                     if obj[4]<=0:
                        # {"feature": "Diarrhea", "instances": 787, "metric_value": 0.865, "depth": 8}
                        if obj[8]<=0:
                           # {"feature": "Tiredness", "instances": 426, "metric_value": 0.9135, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 316, "metric_value": 0.9906, "depth": 10}
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
                           # {"feature": "Tiredness", "instances": 361, "metric_value": 0.7921, "depth": 9}
                           if obj[1]<=0:
                              return 'yes'
                           elif obj[1]>0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 175, "metric_value": 0.9998, "depth": 10}
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
               # {"feature": "Sore-Throat", "instances": 3274, "metric_value": 0.9733, "depth": 5}
               if obj[4]<=0:
                  # {"feature": "Runny-Nose", "instances": 1669, "metric_value": 0.3968, "depth": 6}
                  if obj[7]<=0:
                     # {"feature": "Dry-Cough", "instances": 876, "metric_value": 0.6087, "depth": 7}
                     if obj[2]<=0:
                        # {"feature": "Tiredness", "instances": 509, "metric_value": 0.8227, "depth": 8}
                        if obj[1]>0:
                           # {"feature": "Diarrhea", "instances": 319, "metric_value": 0.9768, "depth": 9}
                           if obj[8]>0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 240, "metric_value": 0.9939, "depth": 10}
                              if obj[3]<=0:
                                 return 'no'
                              else:
                                 return 'no'
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
                  elif obj[7]>0:
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[4]>0:
                  # {"feature": "Difficulty-in-Breathing", "instances": 1605, "metric_value": 0.8227, "depth": 6}
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
            # {"feature": "Runny-Nose", "instances": 5155, "metric_value": 0.8842, "depth": 4}
            if obj[7]<=0:
               # {"feature": "Dry-Cough", "instances": 3290, "metric_value": 0.9945, "depth": 5}
               if obj[2]<=0:
                  # {"feature": "Difficulty-in-Breathing", "instances": 2417, "metric_value": 0.8271, "depth": 6}
                  if obj[3]<=0:
                     # {"feature": "Fever", "instances": 2234, "metric_value": 0.7212, "depth": 7}
                     if obj[0]<=0:
                        # {"feature": "Sore-Throat", "instances": 2058, "metric_value": 0.5607, "depth": 8}
                        if obj[4]<=0:
                           # {"feature": "Tiredness", "instances": 1966, "metric_value": 0.4383, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Diarrhea", "instances": 1582, "metric_value": 0.3226, "depth": 10}
                              if obj[8]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[1]>0:
                              # {"feature": "Diarrhea", "instances": 384, "metric_value": 0.7626, "depth": 10}
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
               # {"feature": "Sore-Throat", "instances": 1865, "metric_value": 0.1972, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Tiredness", "instances": 1828, "metric_value": 0.087, "depth": 6}
                  if obj[1]>0:
                     # {"feature": "Difficulty-in-Breathing", "instances": 1819, "metric_value": 0.0533, "depth": 7}
                     if obj[3]<=0:
                        return 'no'
                     elif obj[3]>0:
                        # {"feature": "Diarrhea", "instances": 256, "metric_value": 0.2557, "depth": 8}
                        if obj[8]>0:
                           # {"feature": "Fever", "instances": 250, "metric_value": 0.1414, "depth": 9}
                           if obj[0]>0:
                              # {"feature": "Dry-Cough", "instances": 248, "metric_value": 0.0944, "depth": 10}
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
      # {"feature": "Nasal-Congestion", "instances": 4728, "metric_value": 0.0161, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Difficulty-in-Breathing", "instances": 4724, "metric_value": 0.0077, "depth": 3}
         if obj[3]<=0:
            # {"feature": "Diarrhea", "instances": 4434, "metric_value": 0.0031, "depth": 4}
            if obj[8]<=0:
               return 'no'
            elif obj[8]>0:
               # {"feature": "Fever", "instances": 1184, "metric_value": 0.0098, "depth": 5}
               if obj[0]>0:
                  return 'no'
               elif obj[0]<=0:
                  # {"feature": "Runny-Nose", "instances": 65, "metric_value": 0.1147, "depth": 6}
                  if obj[7]<=0:
                     return 'no'
                  elif obj[7]>0:
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'no'
            else:
               return 'no'
         elif obj[3]>0:
            # {"feature": "Fever", "instances": 290, "metric_value": 0.0594, "depth": 4}
            if obj[0]>0:
               return 'no'
            elif obj[0]<=0:
               # {"feature": "Sore-Throat", "instances": 79, "metric_value": 0.1703, "depth": 5}
               if obj[4]<=0:
                  return 'no'
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
