def findDecision(obj): #obj[0]: Fever, obj[1]: Tiredness, obj[2]: Dry-Cough, obj[3]: Difficulty-in-Breathing, obj[4]: Sore-Throat, obj[5]: Pains, obj[6]: Nasal-Congestion, obj[7]: Runny-Nose, obj[8]: Diarrhea, obj[9]: Smell and taste loss
   # {"feature": "Smell and taste loss", "instances": 26739, "metric_value": 0.9511, "depth": 1}
   if obj[9]>0:
      # {"feature": "Nasal-Congestion", "instances": 22033, "metric_value": 0.7893, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Difficulty-in-Breathing", "instances": 13039, "metric_value": 0.9708, "depth": 3}
         if obj[3]<=0:
            # {"feature": "Sore-Throat", "instances": 8882, "metric_value": 0.9912, "depth": 4}
            if obj[4]<=0:
               # {"feature": "Pains", "instances": 5541, "metric_value": 0.9523, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Runny-Nose", "instances": 3066, "metric_value": 0.4495, "depth": 6}
                  if obj[7]<=0:
                     # {"feature": "Dry-Cough", "instances": 1642, "metric_value": 0.6699, "depth": 7}
                     if obj[2]<=0:
                        # {"feature": "Tiredness", "instances": 1058, "metric_value": 0.8446, "depth": 8}
                        if obj[1]>0:
                           # {"feature": "Diarrhea", "instances": 618, "metric_value": 0.9365, "depth": 9}
                           if obj[8]>0:
                              # {"feature": "Fever", "instances": 435, "metric_value": 1.0, "depth": 10}
                              if obj[0]>0:
                                 return 'no'
                              elif obj[0]<=0:
                                 return 'yes'
                              else:
                                 return 'yes'
                           elif obj[8]<=0:
                              return 'yes'
                           else:
                              return 'yes'
                        elif obj[1]<=0:
                           # {"feature": "Diarrhea", "instances": 440, "metric_value": 0.6321, "depth": 9}
                           if obj[8]<=0:
                              # {"feature": "Fever", "instances": 255, "metric_value": 0.8479, "depth": 10}
                              if obj[0]<=0:
                                 return 'yes'
                              elif obj[0]>0:
                                 return 'yes'
                              else:
                                 return 'yes'
                           elif obj[8]>0:
                              return 'yes'
                           else:
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
               elif obj[5]>0:
                  # {"feature": "Fever", "instances": 2475, "metric_value": 0.8598, "depth": 6}
                  if obj[0]<=0:
                     # {"feature": "Dry-Cough", "instances": 2175, "metric_value": 0.6895, "depth": 7}
                     if obj[2]<=0:
                        # {"feature": "Tiredness", "instances": 1988, "metric_value": 0.4928, "depth": 8}
                        if obj[1]<=0:
                           # {"feature": "Runny-Nose", "instances": 1544, "metric_value": 0.3486, "depth": 9}
                           if obj[7]<=0:
                              # {"feature": "Diarrhea", "instances": 1539, "metric_value": 0.3368, "depth": 10}
                              if obj[8]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[7]>0:
                              return 'yes'
                           else:
                              return 'yes'
                        elif obj[1]>0:
                           # {"feature": "Runny-Nose", "instances": 444, "metric_value": 0.8183, "depth": 9}
                           if obj[7]<=0:
                              # {"feature": "Diarrhea", "instances": 442, "metric_value": 0.8131, "depth": 10}
                              if obj[8]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[7]>0:
                              return 'yes'
                           else:
                              return 'yes'
                        else:
                           return 'no'
                     elif obj[2]>0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[0]>0:
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'no'
            elif obj[4]>0:
               # {"feature": "Fever", "instances": 3341, "metric_value": 0.5876, "depth": 5}
               if obj[0]>0:
                  return 'no'
               elif obj[0]<=0:
                  # {"feature": "Tiredness", "instances": 1035, "metric_value": 0.9944, "depth": 6}
                  if obj[1]>0:
                     return 'no'
                  elif obj[1]<=0:
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'no'
            else:
               return 'no'
         elif obj[3]>0:
            # {"feature": "Pains", "instances": 4157, "metric_value": 0.3569, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Dry-Cough", "instances": 3145, "metric_value": 0.1642, "depth": 5}
               if obj[2]>0:
                  return 'yes'
               elif obj[2]<=0:
                  # {"feature": "Sore-Throat", "instances": 884, "metric_value": 0.4229, "depth": 6}
                  if obj[4]<=0:
                     # {"feature": "Diarrhea", "instances": 478, "metric_value": 0.6319, "depth": 7}
                     if obj[8]<=0:
                        # {"feature": "Runny-Nose", "instances": 267, "metric_value": 0.8617, "depth": 8}
                        if obj[7]<=0:
                           # {"feature": "Fever", "instances": 181, "metric_value": 0.9814, "depth": 9}
                           if obj[0]<=0:
                              # {"feature": "Tiredness", "instances": 181, "metric_value": 0.9814, "depth": 10}
                              if obj[1]<=0:
                                 return 'yes'
                              else:
                                 return 'yes'
                           else:
                              return 'yes'
                        elif obj[7]>0:
                           return 'yes'
                        else:
                           return 'yes'
                     elif obj[8]>0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[4]>0:
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'yes'
            elif obj[5]>0:
               # {"feature": "Diarrhea", "instances": 1012, "metric_value": 0.727, "depth": 5}
               if obj[8]<=0:
                  return 'yes'
               elif obj[8]>0:
                  # {"feature": "Fever", "instances": 212, "metric_value": 0.2093, "depth": 6}
                  if obj[0]>0:
                     # {"feature": "Tiredness", "instances": 206, "metric_value": 0.0443, "depth": 7}
                     if obj[1]<=1:
                        # {"feature": "Dry-Cough", "instances": 206, "metric_value": 0.0443, "depth": 8}
                        if obj[2]<=1:
                           # {"feature": "Sore-Throat", "instances": 206, "metric_value": 0.0443, "depth": 9}
                           if obj[4]<=1:
                              # {"feature": "Runny-Nose", "instances": 206, "metric_value": 0.0443, "depth": 10}
                              if obj[7]<=1:
                                 return 'no'
                              else:
                                 return 'no'
                           else:
                              return 'no'
                        else:
                           return 'no'
                     else:
                        return 'no'
                  elif obj[0]<=0:
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'no'
            else:
               return 'yes'
         else:
            return 'yes'
      elif obj[6]>0.0:
         return 'yes'
      else:
         return 'yes'
   elif obj[9]<=0:
      # {"feature": "Nasal-Congestion", "instances": 4706, "metric_value": 0.0238, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Sore-Throat", "instances": 4701, "metric_value": 0.0141, "depth": 3}
         if obj[4]>0:
            # {"feature": "Difficulty-in-Breathing", "instances": 2775, "metric_value": 0.0046, "depth": 4}
            if obj[3]<=0:
               return 'no'
            elif obj[3]>0:
               # {"feature": "Fever", "instances": 199, "metric_value": 0.0456, "depth": 5}
               if obj[0]>0:
                  return 'no'
               elif obj[0]<=0:
                  return 'yes'
               else:
                  return 'yes'
            else:
               return 'no'
         elif obj[4]<=0:
            # {"feature": "Dry-Cough", "instances": 1926, "metric_value": 0.026, "depth": 4}
            if obj[2]<=0:
               # {"feature": "Fever", "instances": 1922, "metric_value": 0.0064, "depth": 5}
               if obj[0]<=0:
                  return 'no'
               elif obj[0]>0:
                  # {"feature": "Pains", "instances": 112, "metric_value": 0.0736, "depth": 6}
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
      elif obj[6]>0.0:
         return 'yes'
      else:
         return 'yes'
   else:
      return 'no'
