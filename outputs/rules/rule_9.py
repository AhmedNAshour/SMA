def findDecision(obj): #obj[0]: Fever, obj[1]: Tiredness, obj[2]: Dry-Cough, obj[3]: Difficulty-in-Breathing, obj[4]: Sore-Throat, obj[5]: Pains, obj[6]: Nasal-Congestion, obj[7]: Runny-Nose, obj[8]: Diarrhea, obj[9]: Smell and taste loss
   # {"feature": "Smell and taste loss", "instances": 26739, "metric_value": 0.9493, "depth": 1}
   if obj[9]>0:
      # {"feature": "Nasal-Congestion", "instances": 22062, "metric_value": 0.786, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Pains", "instances": 13050, "metric_value": 0.9689, "depth": 3}
         if obj[5]<=0:
            # {"feature": "Fever", "instances": 7810, "metric_value": 0.7157, "depth": 4}
            if obj[0]<=0:
               # {"feature": "Dry-Cough", "instances": 4519, "metric_value": 0.2605, "depth": 5}
               if obj[2]>0:
                  return 'yes'
               elif obj[2]<=0:
                  # {"feature": "Runny-Nose", "instances": 2181, "metric_value": 0.4406, "depth": 6}
                  if obj[7]<=0:
                     # {"feature": "Sore-Throat", "instances": 1184, "metric_value": 0.6533, "depth": 7}
                     if obj[4]<=0:
                        # {"feature": "Diarrhea", "instances": 802, "metric_value": 0.8083, "depth": 8}
                        if obj[8]<=0:
                           # {"feature": "Tiredness", "instances": 440, "metric_value": 0.8785, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 334, "metric_value": 0.9662, "depth": 10}
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
                           # {"feature": "Tiredness", "instances": 362, "metric_value": 0.6969, "depth": 9}
                           if obj[1]<=0:
                              return 'yes'
                           elif obj[1]>0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 172, "metric_value": 0.9682, "depth": 10}
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
               # {"feature": "Sore-Throat", "instances": 3291, "metric_value": 0.9748, "depth": 5}
               if obj[4]<=0:
                  # {"feature": "Dry-Cough", "instances": 1702, "metric_value": 0.3546, "depth": 6}
                  if obj[2]<=0:
                     # {"feature": "Tiredness", "instances": 904, "metric_value": 0.5467, "depth": 7}
                     if obj[1]>0:
                        # {"feature": "Runny-Nose", "instances": 504, "metric_value": 0.7713, "depth": 8}
                        if obj[7]<=0:
                           # {"feature": "Diarrhea", "instances": 301, "metric_value": 0.9571, "depth": 9}
                           if obj[8]>0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 210, "metric_value": 0.9947, "depth": 10}
                              if obj[3]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[8]<=0:
                              return 'yes'
                           else:
                              return 'yes'
                        elif obj[7]>0:
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
                  # {"feature": "Difficulty-in-Breathing", "instances": 1589, "metric_value": 0.7764, "depth": 6}
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
            # {"feature": "Runny-Nose", "instances": 5240, "metric_value": 0.8882, "depth": 4}
            if obj[7]<=0:
               # {"feature": "Dry-Cough", "instances": 3368, "metric_value": 0.9957, "depth": 5}
               if obj[2]<=0:
                  # {"feature": "Sore-Throat", "instances": 2486, "metric_value": 0.8419, "depth": 6}
                  if obj[4]<=0:
                     # {"feature": "Fever", "instances": 2276, "metric_value": 0.7279, "depth": 7}
                     if obj[0]<=0:
                        # {"feature": "Difficulty-in-Breathing", "instances": 2094, "metric_value": 0.5675, "depth": 8}
                        if obj[3]<=0:
                           # {"feature": "Tiredness", "instances": 2004, "metric_value": 0.4523, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Diarrhea", "instances": 1624, "metric_value": 0.3065, "depth": 10}
                              if obj[8]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[1]>0:
                              # {"feature": "Diarrhea", "instances": 380, "metric_value": 0.8354, "depth": 10}
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
               # {"feature": "Sore-Throat", "instances": 1872, "metric_value": 0.172, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Tiredness", "instances": 1837, "metric_value": 0.0607, "depth": 6}
                  if obj[1]>0:
                     # {"feature": "Difficulty-in-Breathing", "instances": 1828, "metric_value": 0.0225, "depth": 7}
                     if obj[3]<=0:
                        return 'no'
                     elif obj[3]>0:
                        # {"feature": "Diarrhea", "instances": 263, "metric_value": 0.1136, "depth": 8}
                        if obj[8]>0:
                           # {"feature": "Fever", "instances": 260, "metric_value": 0.0364, "depth": 9}
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
      # {"feature": "Nasal-Congestion", "instances": 4677, "metric_value": 0.0182, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Pains", "instances": 4674, "metric_value": 0.0121, "depth": 3}
         if obj[5]>0:
            return 'no'
         elif obj[5]<=0:
            # {"feature": "Sore-Throat", "instances": 1442, "metric_value": 0.0333, "depth": 4}
            if obj[4]>0:
               # {"feature": "Fever", "instances": 1129, "metric_value": 0.0103, "depth": 5}
               if obj[0]>0:
                  return 'no'
               elif obj[0]<=0:
                  return 'yes'
               else:
                  return 'yes'
            elif obj[4]<=0:
               # {"feature": "Dry-Cough", "instances": 313, "metric_value": 0.0987, "depth": 5}
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
