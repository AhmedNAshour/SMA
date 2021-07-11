def findDecision(obj): #obj[0]: Fever, obj[1]: Tiredness, obj[2]: Dry-Cough, obj[3]: Difficulty-in-Breathing, obj[4]: Sore-Throat, obj[5]: Pains, obj[6]: Nasal-Congestion, obj[7]: Runny-Nose, obj[8]: Diarrhea, obj[9]: Smell and taste loss
   # {"feature": "Smell and taste loss", "instances": 26739, "metric_value": 0.9506, "depth": 1}
   if obj[9]>0:
      # {"feature": "Nasal-Congestion", "instances": 22033, "metric_value": 0.7874, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Pains", "instances": 13010, "metric_value": 0.9702, "depth": 3}
         if obj[5]<=0:
            # {"feature": "Fever", "instances": 7783, "metric_value": 0.7207, "depth": 4}
            if obj[0]<=0:
               # {"feature": "Dry-Cough", "instances": 4505, "metric_value": 0.2871, "depth": 5}
               if obj[2]>0:
                  return 'yes'
               elif obj[2]<=0:
                  # {"feature": "Runny-Nose", "instances": 2204, "metric_value": 0.477, "depth": 6}
                  if obj[7]<=0:
                     # {"feature": "Sore-Throat", "instances": 1213, "metric_value": 0.6937, "depth": 7}
                     if obj[4]<=0:
                        # {"feature": "Diarrhea", "instances": 831, "metric_value": 0.8443, "depth": 8}
                        if obj[8]<=0:
                           # {"feature": "Tiredness", "instances": 474, "metric_value": 0.8981, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 385, "metric_value": 0.9628, "depth": 10}
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
                           # {"feature": "Tiredness", "instances": 357, "metric_value": 0.7522, "depth": 9}
                           if obj[1]<=0:
                              return 'yes'
                           elif obj[1]>0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 170, "metric_value": 0.9936, "depth": 10}
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
               # {"feature": "Sore-Throat", "instances": 3278, "metric_value": 0.9735, "depth": 5}
               if obj[4]<=0:
                  # {"feature": "Runny-Nose", "instances": 1693, "metric_value": 0.3844, "depth": 6}
                  if obj[7]<=0:
                     # {"feature": "Dry-Cough", "instances": 908, "metric_value": 0.5839, "depth": 7}
                     if obj[2]<=0:
                        # {"feature": "Tiredness", "instances": 517, "metric_value": 0.8043, "depth": 8}
                        if obj[1]>0:
                           # {"feature": "Diarrhea", "instances": 319, "metric_value": 0.9698, "depth": 9}
                           if obj[8]>0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 232, "metric_value": 0.9935, "depth": 10}
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
                  # {"feature": "Difficulty-in-Breathing", "instances": 1585, "metric_value": 0.8009, "depth": 6}
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
            # {"feature": "Runny-Nose", "instances": 5227, "metric_value": 0.8866, "depth": 4}
            if obj[7]<=0:
               # {"feature": "Dry-Cough", "instances": 3319, "metric_value": 0.9962, "depth": 5}
               if obj[2]<=0:
                  # {"feature": "Fever", "instances": 2435, "metric_value": 0.84, "depth": 6}
                  if obj[0]<=0:
                     # {"feature": "Sore-Throat", "instances": 2249, "metric_value": 0.7387, "depth": 7}
                     if obj[4]<=0:
                        # {"feature": "Difficulty-in-Breathing", "instances": 2065, "metric_value": 0.579, "depth": 8}
                        if obj[3]<=0:
                           # {"feature": "Tiredness", "instances": 1971, "metric_value": 0.4591, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Diarrhea", "instances": 1589, "metric_value": 0.3463, "depth": 10}
                              if obj[8]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[1]>0:
                              # {"feature": "Diarrhea", "instances": 382, "metric_value": 0.7786, "depth": 10}
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
                     elif obj[4]>0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[0]>0:
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[2]>0:
                  return 'yes'
               else:
                  return 'yes'
            elif obj[7]>0:
               # {"feature": "Sore-Throat", "instances": 1908, "metric_value": 0.1804, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Tiredness", "instances": 1871, "metric_value": 0.0673, "depth": 6}
                  if obj[1]>0:
                     # {"feature": "Difficulty-in-Breathing", "instances": 1863, "metric_value": 0.0357, "depth": 7}
                     if obj[3]<=0:
                        return 'no'
                     elif obj[3]>0:
                        # {"feature": "Fever", "instances": 248, "metric_value": 0.1854, "depth": 8}
                        if obj[0]>0:
                           # {"feature": "Diarrhea", "instances": 244, "metric_value": 0.0957, "depth": 9}
                           if obj[8]>0:
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
      elif obj[6]>0.0:
         return 'yes'
      else:
         return 'yes'
   elif obj[9]<=0:
      # {"feature": "Nasal-Congestion", "instances": 4706, "metric_value": 0.0099, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Difficulty-in-Breathing", "instances": 4704, "metric_value": 0.0054, "depth": 3}
         if obj[3]<=0:
            return 'no'
         elif obj[3]>0:
            # {"feature": "Fever", "instances": 293, "metric_value": 0.0589, "depth": 4}
            if obj[0]>0:
               return 'no'
            elif obj[0]<=0:
               # {"feature": "Dry-Cough", "instances": 63, "metric_value": 0.2031, "depth": 5}
               if obj[2]<=0:
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
   else:
      return 'no'
