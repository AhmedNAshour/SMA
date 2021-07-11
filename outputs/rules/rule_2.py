def findDecision(obj): #obj[0]: Fever, obj[1]: Tiredness, obj[2]: Dry-Cough, obj[3]: Difficulty-in-Breathing, obj[4]: Sore-Throat, obj[5]: Pains, obj[6]: Nasal-Congestion, obj[7]: Runny-Nose, obj[8]: Diarrhea, obj[9]: Smell and taste loss
   # {"feature": "Smell and taste loss", "instances": 26739, "metric_value": 0.9497, "depth": 1}
   if obj[9]>0:
      # {"feature": "Nasal-Congestion", "instances": 21990, "metric_value": 0.7824, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Pains", "instances": 12859, "metric_value": 0.9695, "depth": 3}
         if obj[5]<=0:
            # {"feature": "Fever", "instances": 7746, "metric_value": 0.7206, "depth": 4}
            if obj[0]<=0:
               # {"feature": "Dry-Cough", "instances": 4438, "metric_value": 0.2601, "depth": 5}
               if obj[2]>0:
                  return 'yes'
               elif obj[2]<=0:
                  # {"feature": "Runny-Nose", "instances": 2136, "metric_value": 0.4408, "depth": 6}
                  if obj[7]<=0:
                     # {"feature": "Sore-Throat", "instances": 1166, "metric_value": 0.6513, "depth": 7}
                     if obj[4]<=0:
                        # {"feature": "Diarrhea", "instances": 778, "metric_value": 0.8123, "depth": 8}
                        if obj[8]<=0:
                           # {"feature": "Tiredness", "instances": 429, "metric_value": 0.8735, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 326, "metric_value": 0.9625, "depth": 10}
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
                           # {"feature": "Tiredness", "instances": 349, "metric_value": 0.7173, "depth": 9}
                           if obj[1]<=0:
                              return 'yes'
                           elif obj[1]>0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 171, "metric_value": 0.973, "depth": 10}
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
               # {"feature": "Sore-Throat", "instances": 3308, "metric_value": 0.9753, "depth": 5}
               if obj[4]<=0:
                  # {"feature": "Diarrhea", "instances": 1696, "metric_value": 0.3796, "depth": 6}
                  if obj[8]>0:
                     # {"feature": "Runny-Nose", "instances": 856, "metric_value": 0.5998, "depth": 7}
                     if obj[7]<=0:
                        # {"feature": "Dry-Cough", "instances": 483, "metric_value": 0.8249, "depth": 8}
                        if obj[2]<=0:
                           # {"feature": "Tiredness", "instances": 302, "metric_value": 0.9785, "depth": 9}
                           if obj[1]>0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 218, "metric_value": 0.9844, "depth": 10}
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
                     elif obj[7]>0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[8]<=0:
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[4]>0:
                  # {"feature": "Difficulty-in-Breathing", "instances": 1612, "metric_value": 0.7962, "depth": 6}
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
            # {"feature": "Runny-Nose", "instances": 5113, "metric_value": 0.8837, "depth": 4}
            if obj[7]<=0:
               # {"feature": "Dry-Cough", "instances": 3294, "metric_value": 0.9942, "depth": 5}
               if obj[2]<=0:
                  # {"feature": "Fever", "instances": 2437, "metric_value": 0.8319, "depth": 6}
                  if obj[0]<=0:
                     # {"feature": "Difficulty-in-Breathing", "instances": 2253, "metric_value": 0.7284, "depth": 7}
                     if obj[3]<=0:
                        # {"feature": "Sore-Throat", "instances": 2069, "metric_value": 0.5641, "depth": 8}
                        if obj[4]<=0:
                           # {"feature": "Tiredness", "instances": 1980, "metric_value": 0.4478, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Diarrhea", "instances": 1585, "metric_value": 0.312, "depth": 10}
                              if obj[8]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[1]>0:
                              # {"feature": "Diarrhea", "instances": 395, "metric_value": 0.8001, "depth": 10}
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
                     elif obj[3]>0:
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
               # {"feature": "Sore-Throat", "instances": 1819, "metric_value": 0.1673, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Tiredness", "instances": 1790, "metric_value": 0.0737, "depth": 6}
                  if obj[1]>0:
                     # {"feature": "Difficulty-in-Breathing", "instances": 1784, "metric_value": 0.05, "depth": 7}
                     if obj[3]<=0:
                        return 'no'
                     elif obj[3]>0:
                        # {"feature": "Fever", "instances": 221, "metric_value": 0.2659, "depth": 8}
                        if obj[0]>0:
                           # {"feature": "Diarrhea", "instances": 214, "metric_value": 0.1064, "depth": 9}
                           if obj[8]>0:
                              # {"feature": "Dry-Cough", "instances": 213, "metric_value": 0.0767, "depth": 10}
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
      elif obj[6]>0.0:
         return 'yes'
      else:
         return 'yes'
   elif obj[9]<=0:
      # {"feature": "Pains", "instances": 4749, "metric_value": 0.0053, "depth": 2}
      if obj[5]>0:
         return 'no'
      elif obj[5]<=0:
         # {"feature": "Fever", "instances": 1449, "metric_value": 0.0151, "depth": 3}
         if obj[0]>0:
            return 'no'
         elif obj[0]<=0:
            # {"feature": "Dry-Cough", "instances": 184, "metric_value": 0.0865, "depth": 4}
            if obj[2]<=0:
               # {"feature": "Sore-Throat", "instances": 183, "metric_value": 0.0489, "depth": 5}
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
   else:
      return 'no'
